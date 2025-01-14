"""
URL configuration for lab3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import *
from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/clients/', ClientListView.as_view(), name='client-list'),
    path('api/flights/', FlightListView.as_view(), name='flight-list'),
    path('api/flight/<str:flight_number>/', FlightViewSet.as_view({'delete': 'destroy', 'put': 'update'}), name='flight-detail'),
    path('api/crew/<str:crew_number>/', CrewViewSet.as_view({'delete': 'destroy', 'put': 'update'}), name='crew-detail'),
    path('api/aircraft/<str:onBoard_number>/', AircraftViewSet.as_view({'delete': 'destroy', 'put': 'update'}), name='aircraft-detail'),
    path('api/aircrafts/', AircraftListView.as_view(), name='aircraft-list'),
    path('api/schedules/', ScheduleListView.as_view(), name='schedule-list'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/current-user/', CurrentUserView.as_view(), name='current-user'),
    path('api/clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('api/tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('api/flights/create/', FlightCreateView.as_view(), name='flight-create'),
    path('api/crews/create/', CrewCreateView.as_view(), name='crew-create'),
    path('api/crews/', CrewListCreateView.as_view(), name='crew-list-create'),
    path('api/employees/', EmployeeListView.as_view(), name='employee-list'),
    path('api/aircrafts/create/', AircraftCreateView.as_view(), name='aircraft-create'),
    path('api/schedules/create/', ScheduleCreateView.as_view(), name='schedule-create'),
    path('api/airports/create/', AirportCreateView.as_view(), name='airport-create'),
    path('api/transit-stops/create/', TransitStopCreateView.as_view(), name='transitstop-create'),
    #Главная страница
    path('api/flights/count', flight_count, name='flight-count'),
    path('api/aircrafts/count', aircraft_count, name='aircraft-count'),
    path('api/employees/count', employee_count, name='employee-count'),
    path('api/aircrafts/numbers', AircraftNumberListView.as_view(), name='aircraft-number-list'),
    path('api/aircrafts/models', AircraftModelListView, name='aircraft-model-list'),
    path('api/companies/names', get_all_companies, name='get_all_companies'),
]
