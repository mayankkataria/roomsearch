from django.shortcuts import get_object_or_404, render, redirect
from django.http import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

bookings_active = False
available_active = False

def test(request):
    pass
#     if request.method == 'POST':
#         # obj = get_object_or_404(AppUser, id=id)
#         # form = UserForm(request.POST or None, instance=obj)
        # name = request.POST['name']
        # email = request.POST['email']
        # password = request.POST['password']
        # re_password = request.POST['re_password']
        # role = request.POST['role']
        # phone = request.POST['phone']
#         # data = {'phone': phone}
#         form = UserForm(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             form.save()
#             messages.success(request, 'Account created successfully')
#             return HttpResponse('Account created successfully')
#         else:
#             print("form is invalid")
#     else:
#         form = UserForm()
#     return render(request, 'test.html', {'form': form})

# common

def login(request):
    messages.info(request, "")
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                email=cd['email'],
                password=cd['password'])
            # if user.is_authenticated:
            #     print("user authenticated")
            # else:
            #     print("user not authenticated")
            # if request.user.is_authenticated:
            #     print("user is authenticated")
            # else:
            #     print("user not auth")

            if AppUser.objects.filter(email__exact=email).exists():
                if AppUser.objects.filter(email__exact=email).get().password == password:
                    UserDetails = AppUser.objects.filter(email__exact=email).get()
                    if UserDetails.role == 'Manager':
                        return redirect('available')
                    else:
                        return redirect('rooms')
                else:
                    messages.info(request, 'Invalid Password')
                    return redirect('login')

            # if user is not None:
            #     if user.is_warden:
            #         return HttpResponse('Invalid Login')
            #     if user.is_active:
            #         login(request, user)
            #         student = request.user.student
            #         return render(request, 'profile.html', {'student': student})
            #     else:
            #         return HttpResponse('Disabled account')
            # else:
            #     return HttpResponse('Invalid Login')
            else:
                messages.info(request, "Email doesn't exist")
                return redirect('login')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    context = {
        'form': form,
        'messages': messages.get_messages(request)
    }
    return render(request, 'common-temp/login.html', context)

def signup(request):
    messages.info(request, "")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        # role = request.POST['role']
        phone = request.POST['phone']
        form = UserForm(request.POST)
        if not phone.isnumeric():
            messages.info(request, "Invalid phone number")
        elif AppUser.objects.filter(email__exact=email).exists():
            messages.info(request, "Email already exists")
        elif password != re_password:
            messages.info(request, "Passwords didn't matched")
        else:
            if form.is_valid():
                # valid form
                form.save()
                UserDetails = AppUser.objects.filter(email__exact=email).get()
                if UserDetails.role == 'Manager':
                    return redirect('available')
                else:
                    return redirect('rooms')
            else:
                # invalid form
                print(form.errors)
        
    else:
        # get method
        form = UserForm()
    context = {
        'messages': messages.get_messages(request),
        'form': form,
    }
    print(messages)
    return render(request, 'common-temp/signup.html', context)

# for customer

@login_required
def rooms(request):
    available_active =True
    return render(request, 'customer-temp/rooms.html', {'bookings_active': bookings_active, 'available_active': available_active})

@login_required
def bookings(request):
    bookings_active = True
    return render(request, 'customer-temp/bookings.html', {'bookings_active': bookings_active, 'available_active': available_active})

# for manager
@login_required
def available(request):
    return render(request, 'manager-temp/available.html')

@login_required
def booked(request):
    return render(request, 'manager-temp/booked.html')
