
# Create your views here.
# booking/views.py

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import BookingForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
 

def home(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'booking/home.html', {'rooms': rooms})


@login_required

def booking_room(request, room_id):
    # Retrieve the room object using room_id
    room = get_object_or_404(Room, id=room_id)

    # Handle form submission if POST request
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process form data (save booking, send confirmation email, etc.)
            # Example: Saving the booking
            booking = form.save(commit=False)
            booking.room = room  # Associate booking with the room
            booking.save()
            # Redirect to a success page or do something else
            return redirect('booking_success')  # Define 'booking_success' URL in urls.py
    else:
        form = BookingForm()  # Create a new form instance

    # Render the booking_room.html template with the room and form
    return render(request, 'booking/booking_room.html', {'room': room, 'form': form})

@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/profile.html', {'bookings': bookings})


def contact(request):
    if request.method == 'POST':
        #Handling the form submission
        name =request.POST.get('name')
        email = request.POST.get('email')
        message =request.POST.get("message")
        return HttpResponse('Thank you for message, your feedback and suggestions are appreciated')
    else:
        return render(request, 'booking/contact.html')

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
