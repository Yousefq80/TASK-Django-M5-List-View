"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from flights.views import BookingList_API_View, FlightList_API_View,flight_create_view,Booking_detail_View,FlightList_detail_View
urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", FlightList_API_View.as_view(),name='flight'),
    path("bookings/", BookingList_API_View.as_view(),name='booking'),
    path("flights/<int:flight_id>/", FlightList_detail_View.as_view(),name='flight_view'),
    path("bookings/<int:booking_id>/", Booking_detail_View.as_view(),name='booking_view'),
    path("flights/add/", flight_create_view.as_view(),name='flight_create'),
    
]
