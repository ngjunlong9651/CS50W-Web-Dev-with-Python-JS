from django.contrib import admin
from .models import Flights, Airport, Passengers
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
admin.site.register(Flights, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passengers)