# Generated by Django 4.0.10 on 2023-03-15 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='house',
            name='realtor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realtor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dong_list',
            name='gu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dong', to='houses.gu_list'),
        ),
    ]
