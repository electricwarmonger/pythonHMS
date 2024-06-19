# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),

]
