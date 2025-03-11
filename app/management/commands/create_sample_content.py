from django.core.management.base import BaseCommand
from app.models import Masjid, Sharhu, Book
from django.utils import timezone
from wagtail.rich_text import RichText
import datetime
import random

class Command(BaseCommand):
    help = 'Creates sample content with masjid foreign keys'

    def handle(self, *args, **options):
        # First, create some masjids
        masjids = [
            {"name": "مسجد الحرم", "location": "مكة"},
            {"name": "المسجد النبوي", "location": "المدينة"},
            {"name": "المسجد الأقصى", "location": "القدس"},
            {"name": "مسجد الإمام", "location": "الرياض"}
        ]
        
        created_masjids = []
        for masjid_data in masjids:
            masjid, created = Masjid.objects.get_or_create(
                name=masjid_data["name"],
                defaults={"location": masjid_data["location"]}
            )
            created_masjids.append(masjid)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created masjid: {masjid.name}'))
        
        # Now create some sample content that references these masjids
        book_titles = [
            "صحيح البخاري",
            "صحيح مسلم",
            "سنن أبي داود",
            "سنن الترمذي",
            "سنن النسائي",
            "سنن ابن ماجه",
            "الموطأ للإمام مالك",
            "مسند الإمام أحمد",
            "صحيح ابن حبان",
            "المستدرك للحاكم"
        ]
        
        authors = [
            "محمد بن إسماعيل البخاري",
            "مسلم بن الحجاج القشيري",
            "أبو داود السجستاني",
            "أبو عيسى الترمذي",
            "أحمد بن شعيب النسائي",
            "محمد بن يزيد ابن ماجه",
            "مالك بن أنس",
            "أحمد بن حنبل",
            "محمد بن حبان",
            "الحاكم النيسابوري"
        ]
        
        # Create 10 sample books
        for i in range(10):
            # Pick a random masjid
            masjid = random.choice(created_masjids)
            
            # Create a sample book
            title = book_titles[i % len(book_titles)]
            author = authors[i % len(authors)]
            book = Book(
                title=title,
                author=author,
                publisher="دار السلام",
                is_featured=(i < 3),  # First 3 are featured
                summary=RichText(f"<p>هذا كتاب {title} للمؤلف {author}. يحتوي على أحاديث صحيحة.</p>")
            )
            book.save()
            self.stdout.write(self.style.SUCCESS(f'Created book: {title}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully created sample content'))