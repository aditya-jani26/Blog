# Generated by Django 5.0.1 on 2024-03-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0037_alter_rating_ratingvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='ratingvalue',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]