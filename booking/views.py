
# Create your views here.
# booking/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import BookingForm

def home(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'booking/home.html', {'rooms': rooms})

@login_required
def book_room(request, room_id):
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
    return render(request, 'booking/profile.html', {'bookings': bookings})


def contact(request):
    return render(request, 'booking/contact.html')