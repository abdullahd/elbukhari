from django.core.management.base import BaseCommand
from app.models import Khutbah, Masjid
from django.utils import timezone
from wagtail.rich_text import RichText
import datetime
import random
import json

class Command(BaseCommand):
    help = 'Creates 10 sample khutbahs with different titles and proper Masjid references'

    def handle(self, *args, **options):
        # Sample titles for the khutbahs in Arabic
        titles = [
            "أهمية التقوى في حياة المسلم",
            "طلب العلم في الإسلام وفضله",
            "حقوق المسلمين على بعضهم البعض",
            "فضائل شهر رمضان المبارك",
            "قصة النبي يوسف عليه السلام",
            "الصبر عند المصائب والشدائد",
            "آداب طالب العلم وواجباته",
            "أهمية الصلاة في حياة المسلم",
            "التفكر في الآخرة وما أعده الله لعباده",
            "صلة الرحم وأهميتها في الإسلام"
        ]
        
        # Sample Arabic tags
        tags = [
            "تقوى", "علم", "أخلاق", "رمضان", "قصص الأنبياء", 
            "صبر", "آداب", "صلاة", "آخرة", "صلة الرحم"
        ]
        
        # Create a base date and then offset for each entry
        base_date = timezone.now().date() - datetime.timedelta(days=90)
            
        # Get available masjids or create if none exist
        masjids = list(Masjid.objects.all())
        if not masjids:
            # Create some masjids if none exist
            masjid_data = [
                {"name": "المسجد الحرام", "location": "مكة المكرمة"},
                {"name": "المسجد النبوي", "location": "المدينة المنورة"},
                {"name": "المسجد الأقصى", "location": "القدس"},
                {"name": "مسجد قباء", "location": "المدينة المنورة"}
            ]
            
            for data in masjid_data:
                masjid = Masjid(name=data["name"], location=data["location"])
                masjid.save()
                masjids.append(masjid)
                self.stdout.write(self.style.SUCCESS(f'Created masjid: {masjid.name}'))
        
        sermon_types = ['jummah', 'eid', 'special', 'other']
        
        # Sample transcript content
        sample_transcript = """
        <p>بسم الله الرحمن الرحيم</p>
        <p>الحمد لله رب العالمين، والصلاة والسلام على أشرف الأنبياء والمرسلين، سيدنا محمد وعلى آله وصحبه أجمعين.</p>
        <p>أما بعد: فاتقوا الله تعالى وأطيعوه، فإن تقوى الله خير زاد، وطاعته أفضل عمل.</p>
        <p>أيها المسلمون: إن موضوع خطبتنا اليوم هو [موضوع الخطبة]، وهو من المواضيع المهمة التي ينبغي علينا أن نتفقه فيها وأن نعمل بما فيها من أحكام وآداب.</p>
        <p>وفي الختام، أسأل الله العظيم رب العرش العظيم أن ينفعنا بما علمنا، وأن يعلمنا ما ينفعنا، وأن يزيدنا علماً وعملاً صالحاً.</p>
        <p>وصلى الله وسلم على نبينا محمد وعلى آله وصحبه أجمعين.</p>
        """
        
        # Create 10 khutbahs with different titles, dates, and masjids
        for i, title in enumerate(titles):
            # Create a date with increasing interval
            khutbah_date = base_date + datetime.timedelta(days=i*7)  # One week interval
            
            # Pick a random masjid
            masjid = random.choice(masjids)
            
            # Determine sermon type
            sermon_type = sermon_types[i % len(sermon_types)]
            
            # Create transcript with the proper title
            customized_transcript = sample_transcript.replace('[موضوع الخطبة]', title)
            
            # Create a new khutbah
            khutbah = Khutbah(
                title=title,
                date=khutbah_date,
                masjid=masjid,
                sermon_type=sermon_type,
                transcript=RichText(customized_transcript),
                is_featured=(i < 3),  # First 3 are featured
                hits=random.randint(10, 1000)  # Random view count
            )
            
            # Create media content
            media_content_data = [
                {
                    'type': 'audio',
                    'value': {
                        'title': f'Audio for {title}',
                        'audio_url': f'https://example.com/sample-khutbah-{i+1}.mp3',
                    },
                    'id': f'audio-{i+1}'
                }
            ]
            
            # Set the media content
            khutbah.media_content = media_content_data
            
            # Save the khutbah first to be able to add tags
            khutbah.save()
            
            # Add tag for the khutbah
            khutbah.tags.add(tags[i])
            
            # If it's one of the first three, add an additional tag for variety
            if i < 3:
                secondary_tag = tags[(i+5) % len(tags)]
                khutbah.tags.add(secondary_tag)
            
            self.stdout.write(self.style.SUCCESS(f'Created khutbah: {title}'))
            
        self.stdout.write(self.style.SUCCESS('Successfully created 10 sample khutbahs')) 