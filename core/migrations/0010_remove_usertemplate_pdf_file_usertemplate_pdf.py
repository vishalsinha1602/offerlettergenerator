# Generated by Django 5.1 on 2024-08-27 11:52

import core.views
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_usertemplate_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertemplate',
            name='pdf_file',
        ),
        migrations.AddField(
            model_name='usertemplate',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=core.views.user_directory_path),
        ),
    ]
