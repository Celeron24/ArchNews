# Generated by Django 5.0.6 on 2024-06-08 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_homepage_index'),
        ('wagtailcore', '0093_uploadedfile'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Index',
            new_name='HomePage',
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page'},
        ),
    ]
