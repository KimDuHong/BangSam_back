# Generated by Django 4.1.7 on 2023-03-11 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Image', to='houses.house')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
