# Generated by Django 4.0.10 on 2023-03-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_rename_keyword_options_rename_is_owner_house_is_host_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='safetyoptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('safetyoption', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='options',
            old_name='name',
            new_name='option',
        ),
    ]