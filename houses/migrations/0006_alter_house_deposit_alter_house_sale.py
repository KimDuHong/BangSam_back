# Generated by Django 4.0.10 on 2023-03-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0005_rename_cell_kind_house_sell_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='deposit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='house',
            name='sale',
            field=models.BigIntegerField(default=0),
        ),
    ]