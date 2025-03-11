from django.utils.translation import gettext_lazy as _
from wagtail.blocks import StructBlock, CharBlock, URLBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import AudioChooserBlock, VideoChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class AudioBlock(StructBlock):
    title = CharBlock(required=False, help_text="Title for this audio")
    audio_file = AudioChooserBlock(required=False, help_text="Select an audio file from media library")
    audio_url = URLBlock(required=False, help_text="Or provide a URL to an external audio file")
    description = RichTextBlock(required=False)
    
    class Meta:
        template = 'blocks/audio_block.html'
        icon = 'fa-volume-up'
        label = _("ملف صوتي")


class VideoBlock(StructBlock):
    title = CharBlock(required=False, help_text="Title for this video")
    video_file = VideoChooserBlock(required=False, help_text="Select a video file from media library")
    video_url = URLBlock(required=False, help_text="Or provide a URL to an external video")
    thumbnail = ImageChooserBlock(required=False)
    description = RichTextBlock(required=False)
    
    class Meta:
        template = 'blocks/video_block.html'
        icon = 'fa-film'
        label = _("فيديو")


class DocumentBlock(StructBlock):
    title = CharBlock(required=False, help_text="Title for this document")
    document = DocumentChooserBlock()
    description = RichTextBlock(required=False)
    
    class Meta:
        template = 'blocks/document_block.html'
        icon = 'fa-file-pdf-o'
        label = _("ملف PDF") 
