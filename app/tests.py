from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from wagtail.models import Page
from wagtail.test.utils import WagtailPageTestCase, WagtailTestUtils
from wagtail.images.tests.utils import get_test_image_file
from wagtail.images.models import Image

from .models import (
    Khutbah, Mohadarah, Sharhu, Motarjmah, Tilawah, 
    Book, Article, Announcement, SocialMedia,
    KhutbahListingPage, MohadarahListingPage, SharhuListingPage,
    MotarjmahListingPage, TilawahListingPage, BookListingPage,
    ArticleListingPage, AnnouncementListingPage
)
import base64
from datetime import timedelta


class BaseModelTestCase(TestCase):
    """Base test case for content models inheriting from BaseModel"""
    
    def setUp(self):
        # Create a test image to use with models
        self.image = Image.objects.create(
            title="Test image",
            file=get_test_image_file(),
        )
    
    def test_model_str_method(self):
        """Test that the __str__ method returns the title"""
        test_title = "Test Title"
        test_date = timezone.now().date()
        
        # Create a test instance for each model
        khutbah = Khutbah.objects.create(title=test_title, date=test_date)
        mohadarah = Mohadarah.objects.create(title=test_title, date=test_date)
        sharhu = Sharhu.objects.create(title=test_title, book_title="Test Book", date=test_date)
        motarjmah = Motarjmah.objects.create(title=test_title, date=test_date)
        tilawah = Tilawah.objects.create(title=test_title, date=test_date)
        book = Book.objects.create(title=test_title, author="Test Author")
        article = Article.objects.create(title=test_title, date=test_date)
        
        # Test __str__ output
        self.assertEqual(str(khutbah), test_title)
        self.assertEqual(str(mohadarah), test_title)
        self.assertEqual(str(sharhu), test_title)
        self.assertEqual(str(motarjmah), test_title)
        self.assertEqual(str(tilawah), test_title)
        self.assertEqual(str(book), test_title)
        self.assertEqual(str(article), test_title)
    
    def test_increment_hits(self):
        """Test that the increment_hits method increases the hit count"""
        test_khutbah = Khutbah.objects.create(title="Test Khutbah", hits=0)
        
        # Make sure initial hits count is 0
        self.assertEqual(test_khutbah.hits, 0)
        
        # Increment hits
        test_khutbah.increment_hits()
        
        # Reload from database to verify
        test_khutbah.refresh_from_db()
        self.assertEqual(test_khutbah.hits, 1)
        
        # Increment again
        test_khutbah.increment_hits()
        test_khutbah.refresh_from_db()
        self.assertEqual(test_khutbah.hits, 2)


class KhutbahModelTest(TestCase):
    """Test specific features of the Khutbah model"""
    
    def test_sermon_type_default(self):
        """Test that sermon_type defaults to 'friday'"""
        khutbah = Khutbah.objects.create(title="Test Khutbah")
        self.assertEqual(khutbah.sermon_type, "friday")
    
    def test_search_fields(self):
        """Test that transcript is included in search fields"""
        transcript_text = "This is a test transcript with searchable content."
        khutbah = Khutbah.objects.create(
            title="Test Khutbah", 
            transcript=transcript_text
        )
        
        # This is a simplified way to verify search fields - in a real application, 
        # you might want to test actual search functionality
        self.assertTrue(hasattr(Khutbah, 'search_fields'))
        self.assertTrue(any('transcript' in str(field) for field in Khutbah.search_fields))


class ListingPageTests(WagtailPageTestCase):
    """Test the listing page models"""
    
    def setUp(self):
        # Find a page to add our test pages to
        self.root_page = Page.objects.get(id=2)  # Usually the home page
        
        # Create some test content
        self.khutbah1 = Khutbah.objects.create(
            title="Friday Khutbah", 
            date=timezone.now().date(),
            sermon_type="friday"
        )
        self.khutbah2 = Khutbah.objects.create(
            title="Eid Khutbah", 
            date=timezone.now().date() - timedelta(days=10),
            sermon_type="eid"
        )
        
        # Create a listing page
        self.khutbah_listing = KhutbahListingPage(
            title="Khutbah Listing",
            intro="<p>Browse our collection of khutbahs</p>"
        )
        self.root_page.add_child(instance=self.khutbah_listing)
    
    def test_get_items(self):
        """Test that get_items returns the correct queryset"""
        items = self.khutbah_listing.get_items()
        self.assertEqual(items.count(), 2)
        self.assertIn(self.khutbah1, items)
        self.assertIn(self.khutbah2, items)
    
    def test_filter_by_search(self):
        """Test search filtering works"""
        queryset = Khutbah.objects.all()
        
        # Search for "friday"
        filtered = self.khutbah_listing.filter_by_search(queryset, "friday")
        self.assertEqual(filtered.count(), 1)
        self.assertEqual(filtered.first(), self.khutbah1)
        
        # Search for "eid"
        filtered = self.khutbah_listing.filter_by_search(queryset, "eid")
        self.assertEqual(filtered.count(), 1)
        self.assertEqual(filtered.first(), self.khutbah2)
        
        # Search for "khutbah" (should match both)
        filtered = self.khutbah_listing.filter_by_search(queryset, "khutbah")
        self.assertEqual(filtered.count(), 2)
    
    def test_get_context(self):
        """Test context data for listing page"""
        request = self.client.get(self.khutbah_listing.url).wsgi_request
        context = self.khutbah_listing.get_context(request)
        
        self.assertIn('items', context)
        self.assertEqual(context['items'].paginator.count, 2)
        self.assertIsNone(context['search_query'])
        self.assertIsNone(context['current_tag'])
        
        # Test with a search query
        request = self.client.get(f"{self.khutbah_listing.url}?q=friday").wsgi_request
        context = self.khutbah_listing.get_context(request)
        self.assertEqual(context['items'].paginator.count, 1)
        self.assertEqual(context['search_query'], 'friday')


class TemplateRenderingTest(TestCase):
    """Test that templates render correctly"""
    
    def test_test_template_renders(self):
        """Test that the test.html template renders successfully"""
        response = self.client.get(reverse('test_template'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Template Loading Works!")
    
    def test_listing_template_exists(self):
        """Test that listing templates exist and can be loaded"""
        # Note: this doesn't test rendering, just that the file can be found
        from django.template.loader import get_template
        
        try:
            template = get_template('pages/khutbah_listing.html')
            self.assertIsNotNone(template)
        except Exception as e:
            self.fail(f"Failed to load template: {e}")
    


class BlockTemplateTest(TestCase):
    """Test the StreamField block templates"""
    
    def test_block_templates_exist(self):
        """Test that block templates exist and can be loaded"""
        from django.template.loader import get_template
        
        templates = [
            'blocks/audio_block.html',
            'blocks/video_block.html',
            'blocks/document_block.html'
        ]
        
        for template_name in templates:
            try:
                template = get_template(template_name)
                self.assertIsNotNone(template)
            except Exception as e:
                self.fail(f"Failed to load template {template_name}: {e}")
