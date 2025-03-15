from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import StructBlock, URLBlock, RichTextBlock
from taggit.managers import TaggableManager
from wagtail.documents.blocks import DocumentChooserBlock
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.models import Page
from django.shortcuts import render
from wagtailmedia.blocks import AudioChooserBlock, VideoChooserBlock 


@register_snippet
class Location(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the location")

    panels = [
        FieldPanel('name')
    ]


class AudioBlock(StructBlock):
    audio_file = AudioChooserBlock(required=False, help_text="Select an audio file from media library")
    
    class Meta:
        icon = 'music'
        template = 'blocks/audio_block.html'
        label = 'Audio'

class VideoBlock(StructBlock):
    video_file = VideoChooserBlock(required=False, help_text="Select a video file from media library")
    video_url = URLBlock(required=False, help_text="Or provide a URL to an external video")

    class Meta:
        icon = 'media'
        template = 'blocks/video_block.html'
        label = 'Video'

class DocumentBlock(StructBlock):
    document = DocumentChooserBlock()
    
    class Meta:
        icon = 'doc-full'
        template = 'blocks/document_block.html'
        label = 'Document'

class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    media_content = StreamField([
        ('audio', AudioBlock()), 
        ('video', VideoBlock()), 
        ('document', DocumentBlock()),
        ('text', RichTextBlock()),
        ], blank=True, use_json_field=True, verbose_name="Media Content")
    date = models.DateField("Publication Date", blank=True, null=True) 
    location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    hits = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField("Muhim", default=False)
    search_notes = RichTextField(blank=True)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('cover_image'),
        FieldPanel('media_content'),
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Date"),
        MultiFieldPanel([
            FieldPanel('hits'),
            FieldPanel('is_featured'),
        ], heading="Metadata"),
    ]
    
    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True

@register_snippet
class Khutbah(BaseModel):

    class Meta:
        verbose_name_plural = "Khutab"

@register_snippet
class Mohadarah(BaseModel):
    
    class Meta:
        verbose_name_plural = "Mohadarat"

@register_snippet
class Sharhu(BaseModel):    
    class Meta:
        verbose_name_plural = "Shroohat"

@register_snippet
class Motarjmah(BaseModel):
    translator = models.CharField(max_length=255, blank=True, null=True)
    
    panels = BaseModel.panels + [
        FieldPanel('translator'),
    ]
    
    class Meta:
        verbose_name_plural = "Motarjmaat"

@register_snippet
class Tilawah(BaseModel):
    class Meta:
        verbose_name_plural = "Tilawaat"

@register_snippet
class Book(BaseModel):
    publisher = models.CharField(max_length=255, blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., First Edition, 2nd Edition")
    publication_year = models.PositiveSmallIntegerField(blank=True, null=True)
  
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
        ], heading="Basic Information"),
        FieldPanel('cover_image'),
        MultiFieldPanel([
            FieldPanel('publisher'),
            FieldPanel('edition'),
            FieldPanel('publication_year'),
        ], heading="Publication Details"),
        FieldPanel('media_content'),
        MultiFieldPanel([
            FieldPanel('hits'),
            FieldPanel('is_featured'),
        ], heading="Metadata"),
    ]
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

@register_snippet
class Article(BaseModel):
    class Meta:
        ordering = ['title']

@register_snippet
class Announcement(BaseModel):    
    # Announcement-specific dates (in addition to the publication date from BaseModel)
    start_date = models.DateField("Start Date", blank=True, null=True, 
                                  help_text="Date when this announcement becomes active")
    end_date = models.DateField("End Date", blank=True, null=True,
                               help_text="Date when this announcement expires")
    
    panels = BaseModel.panels + [
        MultiFieldPanel([
            FieldPanel('start_date'),
            FieldPanel('end_date'),
        ], heading="Announcement Period"),
    ]
    
    def is_active(self):
        today = timezone.now().date()
        
        if self.start_date and self.end_date:
            return self.start_date <= today <= self.end_date
        elif self.start_date:
            return self.start_date <= today
        elif self.end_date:
            return today <= self.end_date
        return True  # No dates set means always active
    
    class Meta:
        ordering = [ '-start_date', 'title']

@register_snippet
class SocialMedia(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the social media platform")
    url = models.URLField(validators=[URLValidator()])
    icon_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', help_text="Upload an icon image")
    icon_class = models.CharField(max_length=100, blank=True, help_text="CSS class for icon (e.g., 'fa fa-twitter' for FontAwesome)")
    
    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        MultiFieldPanel([
            FieldPanel('icon_image'),
            FieldPanel('icon_class'),
        ], heading="Display Options"),
    ]
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class ListingPage(Page):
    
    class Meta:
        abstract = True
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        
        # Get all instances of the content type
        items = self.get_items()
        
        # Filter by tag if specified
        tag = request.GET.get('tag')
        if tag:
            items = items.filter(tags__name=tag)
        
        # Handle search query
        search_query = request.GET.get('q', None)
        if search_query:
            # Replace filter_by_search call with direct queryset filtering
            items = items.filter(title__icontains=search_query)
            
        # Sort items
        sort = request.GET.get('sort', '-date')
        if sort:
            if sort == 'title':
                items = items.order_by('title')
            elif sort == '-title':
                items = items.order_by('-title')
            elif sort == 'date':
                items = items.order_by('date')
            elif sort == '-date':
                items = items.order_by('-date')
            elif sort == 'hits':
                items = items.order_by('-hits')
        
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(items, 12)  # 12 items per page
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
            
        context['items'] = items
        context['search_query'] = search_query
        context['current_tag'] = tag
        context['current_sort'] = sort
        
        return context
    
    def get_items(self):
        return []
    
    
    def serve(self, request):
        context = self.get_context(request)
        return render(request, self.template, context)

class ArticlePage(Page):
    article = models.ForeignKey('Article', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    
    content_panels = Page.content_panels + [
        FieldPanel('article'),
    ]
    
    