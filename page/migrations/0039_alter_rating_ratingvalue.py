# Generated by Django 5.0.1 on 2024-03-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0038_alter_rating_ratingvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='ratingvalue',
            field=models.IntegerField(default=0),
        ),
    ]