from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Flights, Airport, Passengers
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
admin.site.register(Flights, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passengers)
>>>>>>> 4a05ac1eccc5b3880cb458b7ad7bebc8679b2532
