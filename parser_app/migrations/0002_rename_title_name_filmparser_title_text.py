# Generated by Django 4.2.4 on 2023-08-30 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmparser',
            old_name='title_name',
            new_name='title_text',
        ),
    ]
