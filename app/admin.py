from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail import hooks

from .models import (
    Khutbah, Mohadarah, Sharhu, Motarjmah, Tilawah, 
    Kitab, Article, Announcement, SocialMedia
)

# Standard Django Admin Registration
admin.site.register(SocialMedia)

# Define all your admin ViewSets
class KhutbahViewSet(SnippetViewSet):
    model = Khutbah
    menu_label = "Khutbahs"
    menu_icon = "doc-full"
    list_display = ('title', 'date', 'masjid', 'sermon_type', 'hits')
    list_filter = ('sermon_type', 'date', 'is_featured')
    search_fields = ('title', 'transcript', 'masjid')
    
class MohadarahViewSet(SnippetViewSet):
    model = Mohadarah
    menu_label = "Lectures"
    menu_icon = "media"
    list_display = ('title', 'date', 'masjid', 'hits')
    list_filter = ('date', 'is_featured')
    search_fields = ('title', 'description', 'masjid')

class SharhuViewSet(SnippetViewSet):
    model = Sharhu
    menu_label = "Books Commentary"
    menu_icon = "doc-full-inverse"
    list_display = ('title', 'book_title', 'author', 'part_number', 'hits')
    list_filter = ('date', 'is_featured')
    search_fields = ('title', 'book_title', 'author')

class MotarjmahViewSet(SnippetViewSet):
    model = Motarjmah
    menu_label = "Translations"
    menu_icon = "site"
    list_display = ('title', 'translator', 'translated_language', 'date', 'hits')
    list_filter = ('translated_language', 'date', 'is_featured')
    search_fields = ('title', 'translator')

class TilawahViewSet(SnippetViewSet):
    model = Tilawah
    menu_label = "Recitations"
    menu_icon = "pick"
    list_display = ('title', 'surah', 'ayat_range', 'date', 'hits')
    list_filter = ('date', 'is_featured')
    search_fields = ('title', 'surah')

class BookViewSet(SnippetViewSet):
    model = Kitab
    menu_label = "Books"
    menu_icon = "book"
    list_display = ('title', 'author', 'publisher', 'publication_year', 'hits')
    list_filter = ('publication_year', 'is_featured')
    search_fields = ('title', 'author', 'publisher', 'summary')

class ArticleViewSet(SnippetViewSet):
    model = Article
    menu_label = "Articles"
    menu_icon = "edit"
    list_display = ('title', 'subtitle', 'date', 'hits')
    list_filter = ('date', 'is_featured')
    search_fields = ('title', 'subtitle', 'body')

class AnnouncementViewSet(SnippetViewSet):
    model = Announcement
    menu_label = "Announcements"
    menu_icon = "warning"
    list_display = ('title', 'start_date', 'end_date', 'priority', 'show_as_banner')
    list_filter = ('priority', 'start_date', 'end_date', 'show_as_banner')
    search_fields = ('title', 'body')

# Register all ViewSets using hooks
@hooks.register('register_snippet_viewsets')
def register_snippet_viewsets():
    return [
        KhutbahViewSet,
        MohadarahViewSet,
        SharhuViewSet,
        MotarjmahViewSet,
        TilawahViewSet,
        BookViewSet,
        ArticleViewSet,
        AnnouncementViewSet,
    ]
