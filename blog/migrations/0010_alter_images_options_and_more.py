# Generated by Django 5.0.3 on 2024-04-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['-created']},
        ),
        migrations.AddIndex(
            model_name='images',
            index=models.Index(fields=['-created'], name='blog_images_created_38becd_idx'),
        ),
    ]