from django.utils.translation import gettext_lazy as _
from wagtail.blocks import StructBlock, CharBlock, URLBlock, RichTextBlock, TextBlock, ChoiceBlock
from wagtailmedia.blocks import AudioChooserBlock, VideoChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class AudioBlock(StructBlock):
    audio_file = AudioChooserBlock(required=False, help_text="Select an audio file from media library")
    
    class Meta:
        icon = 'music'
        template = 'blocks/audio_block.html'
        label = 'Audio'


class VideoBlock(StructBlock):
    video_file = VideoChooserBlock(required=False, help_text="Select a video file from media library")
    video_url = URLBlock(required=False, help_text="Or provide a URL to an external video")

    class Meta:
        icon = 'media'
        template = 'blocks/video_block.html'
        label = 'Video'


class DocumentBlock(StructBlock):
    document = DocumentChooserBlock()
    
    class Meta:
        icon = 'doc-full'
        template = 'blocks/document_block.html'
        label = 'Document'


class LinkBlock(StructBlock):
    text = CharBlock(label="link text", required=False)
    url = TextBlock(label="Enter a valid URL", required=False)


class IconBlock(LinkBlock):
    class Icon:
        CHOICES = (
            ('fas fa-envelope', 'Mail'),
            ('fa-brands fa-facebook-f', 'Facebook'),
            ('fa-brands fa-x-twitter', 'Twitter'),
        )
    icon_class = ChoiceBlock(blank=True, null=True, choices=Icon.CHOICES, help_text='Choose a Icon')
