# Generated by Django 5.0.1 on 2024-03-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]