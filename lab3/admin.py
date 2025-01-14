from django.contrib import admin
from .models import *

admin.site.register(AircraftModel)
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Schedule)
admin.site.register(TransitStop)
admin.site.register(Employee)