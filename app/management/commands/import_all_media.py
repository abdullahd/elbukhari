import os
from django.core.management.base import BaseCommand
from django.core.files import File
from wagtailmedia.models import Media

class Command(BaseCommand):
    help = 'Imports all audio files from a specified folder into wagtailmedia'

    def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='Path to the folder containing audio files')

    def handle(self, *args, **options):
        folder_path = options['folder_path']
        
        if not os.path.exists(folder_path):
            self.stdout.write(self.style.ERROR(f"Folder {folder_path} does not exist"))
            return

        # Supported audio extensions from wagtailmedia settings
        audio_extensions = ['.aac', '.aiff', '.flac', '.m4a', '.m4b', '.mp3', '.ogg', '.wav']

        # Iterate through files in the folder
        for filename in os.listdir(folder_path):
            if any(filename.lower().endswith(ext) for ext in audio_extensions):
                file_path = os.path.join(folder_path, filename)
                
                # Open the file and create a Media object
                with open(file_path, 'rb') as f:
                    media_file = File(f, name=filename)
                    media = Media(
                        title=filename,
                        file=media_file,
                        type='audio'
                        )
                    media.save()
                    self.stdout.write(self.style.SUCCESS(f"Imported {filename}"))

        self.stdout.write(self.style.SUCCESS("Import completed"))

#python manage.py import_all_media "C:\Users\abdullahd\Documents\v1_manual\audios"