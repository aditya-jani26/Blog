# Generated by Django 5.0.1 on 2024-03-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0023_alter_comment_commentcontent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentContent',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
    ]