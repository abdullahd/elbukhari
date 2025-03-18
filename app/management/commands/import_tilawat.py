from django.core.management.base import BaseCommand
from wagtail.documents.models import Document
from app.models import * 
from wagtail.blocks import StreamBlockValidationError
from wagtail.fields import StreamField
from wagtail import blocks
from wagtailmedia.blocks import AudioChooserBlock, VideoChooserBlock
from wagtailmedia.models import Media

class Command(BaseCommand):
    help = 'Insert audios'

    def add_audios(self, audios, ModelName):
        for title, filename in audios:
            try:
                document = Media.objects.get(file__endswith=filename)
                
                media_content = StreamField([
                    ('audio', blocks.StructBlock([
                        ('audio_file', AudioChooserBlock()),
                    ]))
                ])
                media_content_value = [
                    {
                        'type': 'audio',
                        'value': {
                            'audio_file': document.id,
                        }
                    }
                ]
                
                audio = ModelName(
                    title=title,
                    media_content=media_content_value
                )
                audio.save()
                
                self.stdout.write(self.style.SUCCESS(f"Inserted '{title}' with file '{filename}'"))
            
            except Document.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Document '{filename}' not found in Wagtail Documents"))
            except StreamBlockValidationError as e:
                self.stdout.write(self.style.ERROR(f"StreamField validation error for '{title}': {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error inserting '{title}': {e}"))

    def handle(self, *args, **options):
        tilawat = [
    ("تلاوة سورة الشرح", "tilawat_sh_bukhary_094_surat_ash_sharh.mp3"),
    ("سورة الفاتحة", "Al-Fatihah.mp3"),
    ("تلاوة من سورة آل عمران من الآية 92 إلى الآية 102", "ali_imran_92-02.mp3"),
    ("تلاوة من سورة الإسراء من الآية 9 إلى الآية 21", "al_isra_9-21.mp3"),
    ("سورة القيامة", "al-qiyamah.mp3"),
    ("سورة الإنفطار", "tilawat_sh_bukhary_082_surat_al_infitar.mp3"),
    ("سورة الأعلى", "Al-Ala.mp3"),
    ("سورة الغاشية", "al-ghashiya.mp3"),
    ("سورة الزلزلة", "tilawat_sh_bukhary_099_surat_al_zilzilah.mp3"),
]

        self.add_audios(audios=tilawat, ModelName=Tilawah)
