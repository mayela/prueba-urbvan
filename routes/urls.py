# -*- coding: utf-8 -*-
from django.conf.urls import url

from routes.views import RouteListAPIView, RouteDetailAPIView
from routes.views import ReservationListAPIView, ReservationDetailAPIView

urlpatterns = [
    url(r'^routes/$', RouteListAPIView.as_view()),
    url(r'^routes/(?P<pk>[0-9]+)/$', RouteDetailAPIView.as_view()),
    url(r'^reservations/$', ReservationListAPIView.as_view()),
    url(r'^reservations/(?P<pk>[0-9]+)/$', ReservationDetailAPIView.as_view()),
]
