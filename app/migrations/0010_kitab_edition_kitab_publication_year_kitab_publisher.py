# Generated by Django 5.1.7 on 2025-03-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_book_kitab'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitab',
            name='edition',
            field=models.CharField(blank=True, help_text='e.g., First Edition, 2nd Edition', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kitab',
            name='publication_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kitab',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
