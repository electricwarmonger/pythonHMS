# booking/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking_room/', views.booking_room, name='booking_room'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact,name='contact'),
    path('login/', views.login_view, name='login'),
       path('signup/', views.signup, name='signup'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)