# Generated by Django 5.0.1 on 2024-03-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_comment_commentersname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
