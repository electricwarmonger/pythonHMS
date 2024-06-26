"""
URL configuration for hotelbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#      path('', include('booking.urls')),  # Include the booking app URLs
# ]

from django.contrib import admin
from django.urls import path, include
from booking import views as booking_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', booking_views.home, name='home'),
    path('profile/', booking_views.profile, name='profile'),
    path('booking_room/', booking_views.booking_room, name='booking_room'),
     path('contact/', booking_views.contact, name='contact'),
       path('signup/', booking_views.signup, name='signup'),
    path('login/', booking_views.login_view, name='login'),
path('confirm_booking/', booking_views.confirm_booking, name='confirm_booking'),

] 