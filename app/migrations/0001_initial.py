# Generated by Django 5.1.7 on 2025-03-11 11:22

import django.core.validators
import django.db.models.deletion
import taggit.managers
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ArticleListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BookListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True, verbose_name='مقدمة الصفحة')),
            ],
            options={
                'verbose_name': 'الصفحة الرئيسية',
                'verbose_name_plural': 'الصفحات الرئيسية',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='KhutbahListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Masjid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='اسم المسجد')),
                ('location', models.CharField(blank=True, max_length=255, verbose_name='الموقع')),
                ('description', wagtail.fields.RichTextField(blank=True, verbose_name='الوصف')),
            ],
            options={
                'verbose_name': 'مسجد',
                'verbose_name_plural': 'المساجد',
            },
        ),
        migrations.CreateModel(
            name='MohadarahListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MotarjmahListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SharhuListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(help_text='Book author name', max_length=255)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.CharField(blank=True, help_text='e.g., First Edition, 2nd Edition', max_length=50, null=True)),
                ('publication_year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('summary', wagtail.fields.RichTextField(blank=True)),
                ('media_content', wagtail.fields.StreamField([('document', 3)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 1: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 2: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 3: ('wagtail.blocks.StructBlock', [[('title', 0), ('document', 1), ('description', 2)]], {})}, verbose_name='Media Content')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['author', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Khutbah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_content', wagtail.fields.StreamField([('audio', 4), ('video', 9), ('document', 12)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this audio', 'required': False}), 1: ('wagtailmedia.blocks.AudioChooserBlock', (), {'help_text': 'Select an audio file from media library', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external audio file', 'required': False}), 3: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('audio_file', 1), ('audio_url', 2), ('description', 3)]], {}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this video', 'required': False}), 6: ('wagtailmedia.blocks.VideoChooserBlock', (), {'help_text': 'Select a video file from media library', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external video', 'required': False}), 8: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('title', 5), ('video_file', 6), ('video_url', 7), ('thumbnail', 8), ('description', 3)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 11: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 12: ('wagtail.blocks.StructBlock', [[('title', 10), ('document', 11), ('description', 3)]], {})}, verbose_name='Media Content')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Muhim')),
                ('search_notes', wagtail.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sermon_type', models.CharField(choices=[('friday', 'Friday Sermon'), ('eid', 'Eid Sermon'), ('other', 'Other Sermon')], default='friday', max_length=100)),
                ('transcript', wagtail.fields.RichTextField(blank=True, null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('masjid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.masjid', verbose_name='المسجد')),
            ],
            options={
                'verbose_name': 'Khutbah',
                'verbose_name_plural': 'Khutab',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_content', wagtail.fields.StreamField([('audio', 4), ('video', 9), ('document', 12)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this audio', 'required': False}), 1: ('wagtailmedia.blocks.AudioChooserBlock', (), {'help_text': 'Select an audio file from media library', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external audio file', 'required': False}), 3: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('audio_file', 1), ('audio_url', 2), ('description', 3)]], {}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this video', 'required': False}), 6: ('wagtailmedia.blocks.VideoChooserBlock', (), {'help_text': 'Select a video file from media library', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external video', 'required': False}), 8: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('title', 5), ('video_file', 6), ('video_url', 7), ('thumbnail', 8), ('description', 3)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 11: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 12: ('wagtail.blocks.StructBlock', [[('title', 10), ('document', 11), ('description', 3)]], {})}, verbose_name='Media Content')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Muhim')),
                ('search_notes', wagtail.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('body', wagtail.fields.RichTextField()),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('masjid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.masjid', verbose_name='المسجد')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_content', wagtail.fields.StreamField([('audio', 4), ('video', 9), ('document', 12)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this audio', 'required': False}), 1: ('wagtailmedia.blocks.AudioChooserBlock', (), {'help_text': 'Select an audio file from media library', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external audio file', 'required': False}), 3: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('audio_file', 1), ('audio_url', 2), ('description', 3)]], {}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this video', 'required': False}), 6: ('wagtailmedia.blocks.VideoChooserBlock', (), {'help_text': 'Select a video file from media library', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external video', 'required': False}), 8: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('title', 5), ('video_file', 6), ('video_url', 7), ('thumbnail', 8), ('description', 3)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 11: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 12: ('wagtail.blocks.StructBlock', [[('title', 10), ('document', 11), ('description', 3)]], {})}, verbose_name='Media Content')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Muhim')),
                ('search_notes', wagtail.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', wagtail.fields.RichTextField()),
                ('start_date', models.DateField(blank=True, help_text='Date when this announcement becomes active', null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, help_text='Date when this announcement expires', null=True, verbose_name='End Date')),
                ('priority', models.CharField(choices=[('0', 'Low'), ('1', 'Medium'), ('2', 'High'), ('3', 'Urgent')], default='medium', max_length=20)),
                ('show_as_banner', models.BooleanField(default=False, help_text='Display as a site-wide banner announcement')),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('masjid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.masjid', verbose_name='المسجد')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
                'ordering': ['-priority', '-start_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Mohadarah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_content', wagtail.fields.StreamField([('audio', 4), ('video', 9), ('document', 12)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this audio', 'required': False}), 1: ('wagtailmedia.blocks.AudioChooserBlock', (), {'help_text': 'Select an audio file from media library', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external audio file', 'required': False}), 3: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('audio_file', 1), ('audio_url', 2), ('description', 3)]], {}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this video', 'required': False}), 6: ('wagtailmedia.blocks.VideoChooserBlock', (), {'help_text': 'Select a video file from media library', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external video', 'required': False}), 8: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('title', 5), ('video_file', 6), ('video_url', 7), ('thumbnail', 8), ('description', 3)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 11: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 12: ('wagtail.blocks.StructBlock', [[('title', 10), ('document', 11), ('description', 3)]], {})}, verbose_name='Media Content')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Muhim')),
                ('search_notes', wagtail.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('masjid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.masjid', verbose_name='المسجد')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Mohadarah',
                'verbose_name_plural': 'Mohadarat',
            },
        ),
        migrations.CreateModel(
            name='Motarjmah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_content', wagtail.fields.StreamField([('audio', 4), ('video', 9), ('document', 12)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this audio', 'required': False}), 1: ('wagtailmedia.blocks.AudioChooserBlock', (), {'help_text': 'Select an audio file from media library', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external audio file', 'required': False}), 3: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('audio_file', 1), ('audio_url', 2), ('description', 3)]], {}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this video', 'required': False}), 6: ('wagtailmedia.blocks.VideoChooserBlock', (), {'help_text': 'Select a video file from media library', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external video', 'required': False}), 8: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('title', 5), ('video_file', 6), ('video_url', 7), ('thumbnail', 8), ('description', 3)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 11: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 12: ('wagtail.blocks.StructBlock', [[('title', 10), ('document', 11), ('description', 3)]], {})}, verbose_name='Media Content')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Muhim')),
                ('search_notes', wagtail.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('translated_language', models.CharField(default='English', max_length=100)),
                ('translator', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('masjid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.masjid', verbose_name='المسجد')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Motarjmah',
                'verbose_name_plural': 'Motarjmaat',
                'ordering': ['-date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Sharhu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_content', wagtail.fields.StreamField([('audio', 4), ('video', 9), ('document', 12)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this audio', 'required': False}), 1: ('wagtailmedia.blocks.AudioChooserBlock', (), {'help_text': 'Select an audio file from media library', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external audio file', 'required': False}), 3: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('audio_file', 1), ('audio_url', 2), ('description', 3)]], {}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this video', 'required': False}), 6: ('wagtailmedia.blocks.VideoChooserBlock', (), {'help_text': 'Select a video file from media library', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external video', 'required': False}), 8: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('title', 5), ('video_file', 6), ('video_url', 7), ('thumbnail', 8), ('description', 3)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 11: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 12: ('wagtail.blocks.StructBlock', [[('title', 10), ('document', 11), ('description', 3)]], {})}, verbose_name='Media Content')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Muhim')),
                ('search_notes', wagtail.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('masjid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.masjid', verbose_name='المسجد')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Sharhu Kitab',
                'verbose_name_plural': 'Sharhu Kutub',
                'ordering': ['book_title'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the social media platform', max_length=100)),
                ('url', models.URLField(validators=[django.core.validators.URLValidator()])),
                ('icon_class', models.CharField(blank=True, help_text="CSS class for icon (e.g., 'fa fa-twitter' for FontAwesome)", max_length=100)),
                ('sort_order', models.PositiveIntegerField(default=0, help_text='Order of display (lower numbers displayed first)')),
                ('color', models.CharField(blank=True, help_text="Color code (e.g., '#1DA1F2' for Twitter blue)", max_length=20)),
                ('icon_image', models.ForeignKey(blank=True, help_text='Upload an icon image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Social Media Link',
                'verbose_name_plural': 'Social Media Links',
                'ordering': ['sort_order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Tilawah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_content', wagtail.fields.StreamField([('audio', 4), ('video', 9), ('document', 12)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this audio', 'required': False}), 1: ('wagtailmedia.blocks.AudioChooserBlock', (), {'help_text': 'Select an audio file from media library', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external audio file', 'required': False}), 3: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('audio_file', 1), ('audio_url', 2), ('description', 3)]], {}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this video', 'required': False}), 6: ('wagtailmedia.blocks.VideoChooserBlock', (), {'help_text': 'Select a video file from media library', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Or provide a URL to an external video', 'required': False}), 8: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('title', 5), ('video_file', 6), ('video_url', 7), ('thumbnail', 8), ('description', 3)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title for this document', 'required': False}), 11: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 12: ('wagtail.blocks.StructBlock', [[('title', 10), ('document', 11), ('description', 3)]], {})}, verbose_name='Media Content')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False, verbose_name='Muhim')),
                ('search_notes', wagtail.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('surah', models.CharField(blank=True, max_length=255, null=True)),
                ('ayat_range', models.CharField(blank=True, help_text='e.g., 1-10', max_length=100, null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('masjid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.masjid', verbose_name='المسجد')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Tilawah',
                'verbose_name_plural': 'Tilawaat',
                'ordering': ['surah', 'ayat_range'],
            },
        ),
    ]
