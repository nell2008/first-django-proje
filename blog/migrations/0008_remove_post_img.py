# Generated by Django 5.0.3 on 2024-04-14 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]
