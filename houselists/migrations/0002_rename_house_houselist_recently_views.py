# Generated by Django 4.1.7 on 2023-03-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houselists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houselist',
            old_name='house',
            new_name='recently_views',
        ),
    ]
