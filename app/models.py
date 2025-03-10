from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from taggit.managers import TaggableManager
from wagtail.search import index 

class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    audio = models.ForeignKey('wagtailmedia.Media', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Audio File")
    video = models.ForeignKey('wagtailmedia.Media', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Video File")
    video_url = models.URLField("External Video URL", blank=True, null=True)
    document = models.ForeignKey('wagtaildocs.Document', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    date = models.DateField("Publication Date", blank=True, null=True) 
    masjid = models.TextField("Masjid", blank=True) 
    makan = models.TextField("Makan", blank=True) 
    hits = models.PositiveIntegerField(default=0)
    muhim = models.BooleanField("Muhim", default=False)
    search_notes = RichTextField(blank=True)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    panels = [
        FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('cover_image'),
            FieldPanel('audio'),
            FieldPanel('video'),
            FieldPanel('video_url'),
            FieldPanel('document'),
        ], heading="Media"),
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('masjid'),
            FieldPanel('makan'),
        ], heading="Location"),
        MultiFieldPanel([
            FieldPanel('hits'),
            FieldPanel('muhim'),
            FieldPanel('search_notes'),
            FieldPanel('tags'),
        ], heading="Metadata"),
    ]
    
    # Proper search fields definition for Wagtail
    search_fields = [
        index.SearchField('title', boost=10),
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
        self.save(update_fields=['hits']) #only update the hits field
    
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
    """Model for longer lectures or educational talks"""
    lecture_series = models.CharField(max_length=255, blank=True, null=True)
    episode_number = models.PositiveIntegerField(blank=True, null=True)
    description = RichTextField(blank=True)
    
    panels = BaseModel.panels + [
        FieldPanel('lecture_series'),
        FieldPanel('episode_number'),
        FieldPanel('description'),
    ]
    
    search_fields = BaseModel.search_fields + [
        index.SearchField('lecture_series'),
        index.SearchField('description'),
    ]
    
    class Meta:
        verbose_name = "Mohadarah"
        verbose_name_plural = "Mohadarat"
        ordering = ['lecture_series', 'episode_number']


@register_snippet
class SharhKitab(BaseModel):
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
        verbose_name = "Sharh Kitab"
        verbose_name_plural = "Sharh Kutub"
        ordering = ['book_title', 'part_number']


@register_snippet
class Motarjmah(BaseModel):
    """Model for translations of texts or speeches"""
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