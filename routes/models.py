# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Route(models.Model):
    name = models.CharField('Route', max_length=45)
    origin = models.IntegerField('Origin')
    destination = models.IntegerField('Destination')
    departure_time = models.DateTimeField('Departure date and time')
    arrival_time = models.DateTimeField('Arrival date and time')

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return self.name


class Reservation(models.Model):
    route = models.ForeignKey('Route', related_name='reservations_by_route')
    user = models.ForeignKey(User, related_name='reservations_by_user')
    pickup = models.IntegerField('Pickup')
    dropoff = models.IntegerField('Dropoff')

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return "{} - {}".format(self.user.username, self.route.name)

