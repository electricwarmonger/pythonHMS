
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


def booking_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        # Store booking details in session
        request.session['booking_details'] = {
            'room_id': room_id,
            'check_in': check_in,
            'check_out': check_out,
        }

        return redirect('confirm_booking')  # Redirect to confirmation page
    else:
        rooms = Room.objects.filter(is_available=True)
        return render(request, 'booking/booking_room.html', {'rooms': rooms})

    
def confirm_booking(request):
    # Retrieve booking details from session
    room_id = request.session.get('room_id')
 
    # Example logic to retrieve room details
    room = Room.objects.get( id=room_id)

    # Render confirm_booking.html with booking details
    return render(request, 'booking/confirm_booking.html', {'room': room})

def confirm_booking(request):
    # Retrieve room_id from session or request.POST
    room_id = request.session.get('room_id')  
    check_in = request.session.get('check_in')
    check_out = request.session.get('check_out')

    # Retrieve the Room object or return 404 if not found
    room = get_object_or_404(Room, id=room_id)

    # Example: Retrieve other necessary data or process booking logic
    # ...

    return render(request, 'booking/confirm_booking.html', {'room': room, 'check_in': check_in, 'check_out': check_out})
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
