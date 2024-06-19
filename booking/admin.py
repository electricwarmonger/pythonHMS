from django.contrib import admin
from .models import Room, Booking, Profile

# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Profile)
# booking/admin.py


admin.site.site_header = "Hotel Booking Administration"
admin.site.site_title = "Hotel Booking Admin Portal"
admin.site.index_title = "Welcome to the Hotel Booking Admin"