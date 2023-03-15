# Generated by Django 4.0.10 on 2023-03-15 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dong_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gu_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('sale', models.PositiveIntegerField(default=0)),
                ('deposit', models.PositiveIntegerField(default=0)),
                ('monthly_rent', models.PositiveIntegerField(default=0)),
                ('maintenance_cost', models.PositiveIntegerField(default=0)),
                ('room', models.PositiveIntegerField(default=0)),
                ('toilet', models.PositiveIntegerField(default=0)),
                ('pyeongsu', models.PositiveIntegerField(default=0)),
                ('distance_to_station', models.PositiveIntegerField(default=0)),
                ('room_kind', models.CharField(choices=[('ONE_ROOM', '원룸'), ('HOME', '주택'), ('APART', '아파트'), ('VILLA', '빌라'), ('OFFICETEL', '오피스텔'), ('SHARE_HOUSE', '쉐어하우스')], max_length=20)),
                ('cell_kind', models.CharField(choices=[('SALE', '매매'), ('CHARTER', '전세'), ('MONTHLY_RENT', '월세')], max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('visited', models.PositiveIntegerField(default=0, editable=False)),
                ('is_sale', models.BooleanField(default=True)),
                ('is_owner', models.BooleanField(default=False)),
                ('dong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.dong_list')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
