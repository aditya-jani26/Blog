# Generated by Django 5.0.1 on 2024-03-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_remove_comment_abc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='uPass',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
