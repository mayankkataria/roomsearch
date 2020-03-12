from django.shortcuts import render
from django.http import *
from .forms import *
from django.contrib import messages

bookings_active = False
available_active = False

# common

def login(request):
    return render(request, 'common-temp/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponse('Account created successfully')
    else:
        form = UserForm()
    return render(request, 'common-temp/signup.html', {'form': form})

# for customer

def rooms(request):
    available_active =True
    return render(request, 'customer-temp/rooms.html', {'bookings_active': bookings_active, 'available_active': available_active})

def bookings(request):
    bookings_active = True
    return render(request, 'customer-temp/bookings.html', {'bookings_active': bookings_active, 'available_active': available_active})

# for manager

def available(request):
    return render(request, 'manager-temp/available.html')

def booked(request):
    return render(request, 'manager-temp/booked.html')