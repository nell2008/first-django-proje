# Generated by Django 5.0.3 on 2024-04-11 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_ticket_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('body', models.TextField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('activ', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='blog_commen_created_79f39f_idx')],
            },
        ),
    ]