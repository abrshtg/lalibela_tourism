# lalibela_tourism/tourism/admin.py

from django.contrib import admin
from .models import Tourist, TourPackage, Attraction, Booking

admin.site.register(Tourist)
admin.site.register(TourPackage)
admin.site.register(Attraction)
admin.site.register(Booking)
