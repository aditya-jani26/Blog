# Generated by Django 5.0.1 on 2024-02-21 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_rename_commants_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
