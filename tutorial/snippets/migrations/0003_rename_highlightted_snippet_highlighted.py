# Generated by Django 4.1 on 2022-09-08 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_highlightted_snippet_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='highlightted',
            new_name='highlighted',
        ),
    ]
