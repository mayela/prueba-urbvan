# -*- coding: utf-8 -*-
from rest_framework import serializers

from django.contrib.auth.models import User

from routes.models import Route, Reservation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
                'id', 
                'name', 
                'origin', 
                'destination', 
                'departure_time', 
                'arrival_time'
                )


class ReservationSerializer(serializers.ModelSerializer):
    route = RouteSerializer()
    user = UserSerializer()
    class Meta:
        model = Reservation
        fields = ('id', 'route', 'user', 'pickup', 'dropoff')
