# Generated by Django 5.0.6 on 2024-06-08 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_options'),
        ('wagtailcore', '0093_uploadedfile'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='Index',
        ),
    ]
