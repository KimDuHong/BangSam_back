# Generated by Django 4.0.10 on 2023-03-22 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0010_remove_house_is_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='distance_to_station',
        ),
    ]
