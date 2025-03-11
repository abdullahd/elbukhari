from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import StructBlock, CharBlock, URLBlock, RichTextBlock
from taggit.managers import TaggableManager
from wagtail.search import index 
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from django.core.validators import URLValidator, EmailValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from wagtail.admin.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.models import Page
from django.shortcuts import render
from wagtailmedia.blocks import AudioChooserBlock, VideoChooserBlock 
from django import forms

# Define custom blocks for StreamField
class AudioBlock(StructBlock):
    title = CharBlock(required=False, help_text="Title for this audio")
    audio_file = AudioChooserBlock(required=False, help_text="Select an audio file from media library")
    audio_url = URLBlock(required=False, help_text="Or provide a URL to an external audio file")
    description = RichTextBlock(required=False)
    
    class Meta:
        icon = 'music'
        template = 'blocks/audio_block.html'
        label = 'Audio'


class VideoBlock(StructBlock):
    title = CharBlock(required=False, help_text="Title for this video")
    video_file = VideoChooserBlock(required=False, help_text="Select a video file from media library")
    video_url = URLBlock(required=False, help_text="Or provide a URL to an external video")
    thumbnail = ImageChooserBlock(required=False)
    description = RichTextBlock(required=False)
    
    class Meta:
        icon = 'media'
        template = 'blocks/video_block.html'
        label = 'Video'


class DocumentBlock(StructBlock):
    title = CharBlock(required=False, help_text="Title for this document")
    document = DocumentChooserBlock()
    description = RichTextBlock(required=False)
    
    class Meta:
        icon = 'doc-full'
        template = 'blocks/document_block.html'
        label = 'Document'


class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    
    # Replace individual media fields with StreamField
    media_content = StreamField([
        ('audio', AudioBlock()),
        ('video', VideoBlock()),
        ('document', DocumentBlock()),
    ], blank=True, use_json_field=True, verbose_name="Media Content")
    
    date = models.DateField("Publication Date", blank=True, null=True) 
    masjid = models.TextField("Masjid", blank=True) 
    makan = models.TextField("Makan", blank=True) 
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
            FieldPanel('masjid'),
            FieldPanel('makan'),
        ], heading="Location"),
        MultiFieldPanel([
            FieldPanel('hits'),
            FieldPanel('is_featured'),
            FieldPanel('search_notes'),
            FieldPanel('tags'),
        ], heading="Metadata"),
    ]
    
    # Update search fields to include StreamField content
    search_fields = [
        index.SearchField('title', boost=10),
        index.SearchField('media_content'),
        index.SearchField('search_notes'),
        index.SearchField('masjid'),
        index.SearchField('makan'),
        index.RelatedFields('tags', [
            index.SearchField('name'),
        ]),
    ]
    
    def __str__(self):
        return self.title
    
    def increment_hits(self):
        self.hits += 1
        self.save(update_fields=['hits'])
    
    class Meta:
        abstract = True


@register_snippet
class Khutbah(BaseModel):
    """Model for Friday sermons or religious lectures"""
    sermon_type = models.CharField(max_length=100, choices=[('friday', 'Friday Sermon'), ('eid', 'Eid Sermon'), ('other', 'Other Sermon')], default='friday')
    transcript = RichTextField(blank=True, null=True)
    
    panels = BaseModel.panels + [
        FieldPanel('sermon_type'),
        FieldPanel('transcript'),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('transcript'),
    ]
    
    class Meta:
        verbose_name = "Khutbah"
        verbose_name_plural = "Khutab"


@register_snippet
class Mohadarah(BaseModel):
    description = RichTextField(blank=True)
    
    panels = BaseModel.panels + [
        FieldPanel('description'),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('description'),
    ]
    
    class Meta:
        verbose_name = "Mohadarah"
        verbose_name_plural = "Mohadarat"


@register_snippet
class Sharhu(BaseModel):
    """Model for book commentary or explanation"""
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    chapter = models.CharField(max_length=255, blank=True, null=True)
    part_number = models.PositiveIntegerField(blank=True, null=True)
    
    panels = BaseModel.panels + [
        FieldPanel('book_title'),
        FieldPanel('author'),
        FieldPanel('chapter'),
        FieldPanel('part_number'),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('book_title'),
        index.SearchField('author'),
        index.SearchField('chapter'),
    ]
    
    class Meta:
        verbose_name = "Sharhu Kitab"
        verbose_name_plural = "Sharhu Kutub"
        ordering = ['book_title', 'part_number']


@register_snippet
class Motarjmah(BaseModel):
    translated_language = models.CharField(max_length=100, default="English")
    translator = models.CharField(max_length=255, blank=True, null=True)
    
    panels = BaseModel.panels + [
        FieldPanel('translated_language'),
        FieldPanel('translator'),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('translator'),
    ]
    
    class Meta:
        verbose_name = "Motarjmah"
        verbose_name_plural = "Motarjmaat"
        ordering = ['-date', 'title']  # Added default ordering


@register_snippet
class Tilawah(BaseModel):
    """Model for Quranic recitations"""
    surah = models.CharField(max_length=255, blank=True, null=True)
    ayat_range = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., 1-10")
    
    panels = BaseModel.panels + [
        FieldPanel('surah'),
        FieldPanel('ayat_range'),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('surah'),
    ]
    
    class Meta:
        verbose_name = "Tilawah"
        verbose_name_plural = "Tilawaat"
        ordering = ['surah', 'ayat_range']  # Added logical ordering


@register_snippet
class Book(models.Model):
    """Model for book entries"""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, help_text="Book author name")
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    publisher = models.CharField(max_length=255, blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., First Edition, 2nd Edition")
    publication_year = models.PositiveSmallIntegerField(blank=True, null=True)
    summary = RichTextField(blank=True)
    
    media_content = StreamField([
        ('document', DocumentBlock()),
    ], blank=True, use_json_field=True, verbose_name="Media Content")
    
    hits = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField("Featured", default=False)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('author'),
        ], heading="Basic Information"),
        
        FieldPanel('cover_image'),
        
        MultiFieldPanel([
            FieldPanel('publisher'),
            FieldPanel('edition'),
            FieldPanel('publication_year'),
        ], heading="Publication Details"),
        
        FieldPanel('summary'),
        FieldPanel('media_content'),
        
        MultiFieldPanel([
            FieldPanel('hits'),
            FieldPanel('is_featured'),
            FieldPanel('tags'),
        ], heading="Metadata"),
    ]
    
    search_fields = [
        index.SearchField('title', boost=10),
        index.SearchField('author', boost=5),
        index.SearchField('publisher'),
        index.SearchField('summary'),
        index.RelatedFields('tags', [
            index.SearchField('name'),
        ]),
    ]
    
    def __str__(self):
        return self.title
    
    def increment_hits(self):
        self.hits += 1
        self.save(update_fields=['hits'])
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['author', 'title']


@register_snippet
class Article(BaseModel):
    """Model for articles or blog posts"""
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField()

    panels = BaseModel.panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('subtitle'),
        index.SearchField('body', boost=2),
    ]
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-date', 'title']


@register_snippet
class Announcement(BaseModel):
    body = RichTextField()
    
    # Announcement-specific dates (in addition to the publication date from BaseModel)
    start_date = models.DateField("Start Date", blank=True, null=True, 
                                  help_text="Date when this announcement becomes active")
    end_date = models.DateField("End Date", blank=True, null=True,
                               help_text="Date when this announcement expires")
    
    # Announcement type/priority
    PRIORITY_CHOICES = [
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ]
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    
    # Whether to show as a banner announcement
    show_as_banner = models.BooleanField(default=False, 
                                        help_text="Display as a site-wide banner announcement")
    
    panels = BaseModel.panels + [
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('start_date'),
            FieldPanel('end_date'),
        ], heading="Announcement Period"),
        MultiFieldPanel([
            FieldPanel('priority'),
            FieldPanel('show_as_banner'),
        ], heading="Display Options"),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('subtitle'),
        index.SearchField('body', boost=2),
    ]
    
    def is_active(self):
        """Check if the announcement is currently active based on dates"""
        today = timezone.now().date()
        
        if self.start_date and self.end_date:
            return self.start_date <= today <= self.end_date
        elif self.start_date:
            return self.start_date <= today
        elif self.end_date:
            return today <= self.end_date
        return True  # No dates set means always active
    
    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
        ordering = ['-priority', '-start_date', 'title']


@register_snippet
class SocialMedia(models.Model):
    """Model for storing social media links and icons"""
    name = models.CharField(max_length=100, help_text="Name of the social media platform")
    url = models.URLField(validators=[URLValidator()])
    
    # Two options for icons - either upload an image or use a CSS class
    icon_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Upload an icon image"
    )
    icon_class = models.CharField(
        max_length=100, 
        blank=True, 
        help_text="CSS class for icon (e.g., 'fa fa-twitter' for FontAwesome)"
    )
    
    # For ordering the social media links
    sort_order = models.PositiveIntegerField(
        default=0, 
        blank=False, 
        null=False,
        help_text="Order of display (lower numbers displayed first)"
    )
    
    # Optional color for styling
    color = models.CharField(
        max_length=20, 
        blank=True, 
        help_text="Color code (e.g., '#1DA1F2' for Twitter blue)"
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        MultiFieldPanel([
            FieldPanel('icon_image'),
            FieldPanel('icon_class'),
            FieldPanel('color'),
        ], heading="Display Options"),
        FieldPanel('sort_order'),
    ]
    
    def __str__(self):
        return self.name
    
    def clean(self):
        """Validate that at least one icon option is provided"""
        super().clean()
        if not self.icon_image and not self.icon_class:
            from django.core.exceptions import ValidationError
            raise ValidationError("Please provide either an icon image or a CSS class.")
    
    class Meta:
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"
        ordering = ['sort_order', 'name']


class ListingPage(Page):
    """Abstract base class for all listing pages"""
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
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
            items = self.filter_by_search(items, search_query)
            
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
        """Override in child classes to return the proper queryset"""
        return []
    
    def filter_by_search(self, queryset, search_term):
        """Default search filter using the search_fields"""
        return queryset.filter(title__icontains=search_term)
    
    def serve(self, request):
        context = self.get_context(request)
        return render(request, self.template, context)


class KhutbahListingPage(ListingPage):
    """Page listing all Khutbah entries"""
    template = "pages/khutbah_listing.html"
    
    def get_items(self):
        return Khutbah.objects.all()
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(transcript__icontains=search_term) |
            models.Q(masjid__icontains=search_term)
        )


class MohadarahListingPage(ListingPage):
    """Page listing all Mohadarah entries"""
    template = "pages/mohadarah_listing.html"
    
    def get_items(self):
        return Mohadarah.objects.all()
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(description__icontains=search_term)
        )


class SharhuListingPage(ListingPage):
    """Page listing all Sharhu Kitab entries"""
    template = "pages/sharhu_listing.html"
    
    def get_items(self):
        return Sharhu.objects.all()
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(book_title__icontains=search_term) |
            models.Q(author__icontains=search_term)
        )


class MotarjmahListingPage(ListingPage):
    """Page listing all Motarjmah entries"""
    template = "pages/motarjmah_listing.html"
    
    def get_items(self):
        return Motarjmah.objects.all()
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(translator__icontains=search_term)
        )


class TilawahListingPage(ListingPage):
    """Page listing all Tilawah entries"""
    template = "pages/tilawah_listing.html"
    
    def get_items(self):
        return Tilawah.objects.all()
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(surah__icontains=search_term)
        )


class BookListingPage(ListingPage):
    """Page listing all Book entries"""
    template = "pages/book_listing.html"
    
    def get_items(self):
        return Book.objects.all()
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(author__icontains=search_term) |
            models.Q(publisher__icontains=search_term) |
            models.Q(summary__icontains=search_term)
        )


class ArticleListingPage(ListingPage):
    """Page listing all Article entries"""
    template = "pages/article_listing.html"
    
    def get_items(self):
        return Article.objects.all()
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(subtitle__icontains=search_term) |
            models.Q(body__icontains=search_term)
        )


class AnnouncementListingPage(ListingPage):
    """Page listing all Announcement entries"""
    template = "pages/announcement_listing.html"
    
    def get_items(self):
        # By default, only show active announcements
        return Announcement.objects.filter(
            models.Q(start_date__isnull=True) |
            models.Q(start_date__lte=timezone.now().date())
        ).filter(
            models.Q(end_date__isnull=True) |
            models.Q(end_date__gte=timezone.now().date())
        )
    
    def filter_by_search(self, queryset, search_term):
        return queryset.filter(
            models.Q(title__icontains=search_term) |
            models.Q(body__icontains=search_term)
        )


