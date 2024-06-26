# Generated by Django 5.0.3 on 2024-04-22 22:33

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_images_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_file',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, scale=None, size=[500, 300], upload_to='post_images'),
        ),
    ]
