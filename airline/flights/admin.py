from django.contrib import admin
from .models import Airport, Flight

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    
class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "city")
    
    
admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
