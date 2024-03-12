# Generated by Django 5.0.1 on 2024-03-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_remove_members_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenterName',
            new_name='commentersName',
        ),
        migrations.AddField(
            model_name='members',
            name='forgetPassToken',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
