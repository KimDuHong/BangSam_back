# Generated by Django 4.1.7 on 2023-03-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houselists', '0002_rename_house_houselist_recently_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='houselist',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
