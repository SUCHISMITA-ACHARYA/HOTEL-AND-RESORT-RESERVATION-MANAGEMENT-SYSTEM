# Generated by Django 5.0.4 on 2024-04-15 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_hotel_detail_address_resort_detail_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('h', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='desc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('h', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=100)),
                ('h', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='rats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.CharField(max_length=100)),
                ('h', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='tora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_room_available', models.CharField(max_length=100)),
                ('h', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
            ],
        ),
    ]