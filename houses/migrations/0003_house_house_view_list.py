# Generated by Django 4.1.7 on 2023-03-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houselists', '0001_initial'),
        ('houses', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='house_view_list',
            field=models.ManyToManyField(related_name='house_view_list', to='houselists.houselist'),
        ),
    ]
