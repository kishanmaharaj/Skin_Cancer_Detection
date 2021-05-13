# Generated by Django 2.1.2 on 2018-11-03 19:04

from django.db import migrations, models
import machina.apps.forum_conversation.forum_attachments.abstract_models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to=machina.apps.forum_conversation.forum_attachments.abstract_models.get_attachment_file_upload_to, verbose_name='File'),
        ),
    ]