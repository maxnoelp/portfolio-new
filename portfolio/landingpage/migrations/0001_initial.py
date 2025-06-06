# Generated by Django 5.1.9 on 2025-05-29 18:04

import django.db.models.deletion
import filer.fields.image
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', tinymce.models.HTMLField(verbose_name='Description')),
                ('url', models.URLField(blank=True, verbose_name='Github URL')),
                ('live_url', models.URLField(blank=True, verbose_name='Live URL')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
                ('image_2', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_2', to=settings.FILER_IMAGE_MODEL, verbose_name='Image 2')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
