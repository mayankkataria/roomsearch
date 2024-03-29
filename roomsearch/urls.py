"""roomsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from roomapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name='test'),
    # common
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # for customer
    path('customer/', views.rooms, name='rooms'),
    path('customer/rooms', views.rooms, name='rooms'),
    path('customer/bookings', views.bookings, name='bookings'),
    # for manager
    path('manager/', views.available, name='available'),
    path('manager/available', views.available, name='available'),
    path('manager/booked', views.booked, name='booked'),
]
