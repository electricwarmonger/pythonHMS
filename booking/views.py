
# Create your views here.
# booking/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import BookingForm
from django.contrib.auth import authenticate, login


def home(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'booking/home.html', {'rooms': rooms})


@login_required
def booking_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            room.available = True
            room.save()
            return redirect('profile')
    else:
        form = BookingForm()
    return render(request, 'booking/book_room.html', {'form': form, 'room': room})

@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/home.html', {'bookings': bookings})


def contact(request):
    if request.method == 'POST':
        #Handling the form submission
        name =request.POST.get('name')
        email = request.POST.get('email')
        message =request.POST.get("message")
        return HttpResponse('Thank you for message, your feedback and suggestions are appreciated')
    else:
        return render(request, 'booking/contact.html')

# booking/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home page after signup
    else:
        form = SignUpForm()
    return render(request, 'booking/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})
