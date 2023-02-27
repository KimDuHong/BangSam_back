# Generated by Django 4.1.7 on 2023-02-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]