# Generated by Django 4.2.6 on 2023-11-06 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anticipatedresponse',
            old_name='level',
            new_name='level_of_understanding',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='level',
            new_name='level_of_understanding',
        ),
        migrations.RenameField(
            model_name='userresponse',
            old_name='level',
            new_name='level_of_understanding',
        ),
    ]