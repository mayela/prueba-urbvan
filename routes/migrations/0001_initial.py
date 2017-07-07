# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 04:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup', models.IntegerField(verbose_name='Pickup')),
                ('dropoff', models.IntegerField(verbose_name='Dropoff')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Route')),
                ('origin', models.IntegerField(verbose_name='Origin')),
                ('destination', models.IntegerField(verbose_name='Destination')),
                ('departure_time', models.DateTimeField(verbose_name='Departure date and time')),
                ('arrival_time', models.DateTimeField(verbose_name='Arrival date and time')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_by_route', to='routes.Route'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
