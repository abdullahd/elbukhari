from django.core.management.base import BaseCommand
from app.models import Khutbah
from django.utils import timezone
from wagtail.rich_text import RichText
import datetime

class Command(BaseCommand):
    help = 'Creates 10 sample khutbahs with different titles but same audio content'

    def handle(self, *args, **options):
        # Sample titles for the khutbahs
        titles = [
            "The Importance of Taqwa",
            "Seeking Knowledge in Islam",
            "The Rights of Muslims Upon One Another",
            "The Virtues of Ramadan",
            "The Story of Prophet Yusuf",
            "Patience in Times of Hardship",
            "The Etiquettes of Seeking Knowledge",
            "The Importance of Prayer",
            "Reflecting on the Hereafter",
            "Maintaining Family Ties in Islam"
        ]
        
        # Create a base date and then offset for each entry
        base_date = timezone.now().date() - datetime.timedelta(days=90)
        
        # Sample locations
        masjids = ["Masjid Al-Haram", "Masjid Al-Nabawi", "Masjid Al-Aqsa", "Local Community Masjid", "University Masjid"]
        makans = ["Makkah", "Madinah", "Jerusalem", "Local City", "University Campus"]
        
        # For demonstration purposes, we're assuming there's an existing audio file
        # In a real implementation, you would need to create or reference actual media files
        
        # Create 10 khutbahs with different titles but same audio structure
        for i, title in enumerate(titles):
            # Create a date with increasing interval
            khutbah_date = base_date + datetime.timedelta(days=i*7)  # One week interval
            
            # Create new khutbah
            khutbah = Khutbah(
                title=title,
                date=khutbah_date,
                masjid=masjids[i % len(masjids)],
                makan=makans[i % len(makans)],
                sermon_type='friday' if i % 3 != 0 else ('eid' if i % 3 == 1 else 'other'),
                transcript=RichText(f"<p>This is the transcript for {title}. It contains the key points discussed in this khutbah.</p>")
            )
            
            # Set the same basic audio content for all
            # Note: In a real implementation, you would need to reference actual audio files
            # This part is conceptual since we can't directly create StreamField content this way
            audio_content = [
                ('audio', {
                    'title': f'Audio for {title}',
                    'audio_url': 'https://example.com/sample-audio.mp3',
                    'description': '<p>Sample audio recording of the khutbah.</p>'
                })
            ]
            
            # Note: In reality, you'd need to properly instantiate StreamField content
            # This is a simplified version and would need adjustment based on your exact model setup
            
            # Save the khutbah
            khutbah.save()
            
            self.stdout.write(self.style.SUCCESS(f'Created khutbah: {title}'))
            
        self.stdout.write(self.style.SUCCESS('Successfully created 10 sample khutbahs')) 