from django.contrib import admin

from routes.models import Route, Reservation


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
