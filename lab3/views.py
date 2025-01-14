from django.http import JsonResponse
from rest_framework import generics, viewsets, status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AircraftListView(APIView):
    def get(self, request):
        aircrafts = Aircraft.objects.all()
        serializer = AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data)
class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def destroy(self, request, *args, **kwargs):
        # Извлекаем рейс по его номеру
        flight_number = kwargs.get('flight_number')
        try:
            flight = Flight.objects.get(flight_number=flight_number)
            flight.delete()  # Удаление рейса
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Flight.DoesNotExist:
            return Response({"detail": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        flight_number = self.kwargs.get('flight_number')
        try:
            flight = Flight.objects.get(flight_number=flight_number)
        except Flight.DoesNotExist:
            return Response({"detail": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FlightSerializerStandart(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewAllSerializer

    def destroy(self, request, *args, **kwargs):
        crew_number = kwargs.get('crew_number')
        try:
            crew = Crew.objects.get(crew_number=crew_number)
            crew.delete()  # Удаление рейса
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Crew.DoesNotExist:
            return Response({"detail": "Crew not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        crew_number = self.kwargs.get('crew_number')
        try:
            crew = Crew.objects.get(crew_number=crew_number)
        except Crew.DoesNotExist:
            return Response({"detail": "Crew not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CrewAllSerializer(crew, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftAllSerializer

    def destroy(self, request, *args, **kwargs):
        onBoard_number = kwargs.get('onBoard_number')
        try:
            aircraft = Aircraft.objects.get(onBoard_number=onBoard_number)
            aircraft.delete()  # Удаление рейса
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Aircraft.DoesNotExist:
            return Response({"detail": "Aircraft not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        onBoard_number = self.kwargs.get('onBoard_number')
        try:
            aircraft = Aircraft.objects.get(onBoard_number=onBoard_number)
        except Aircraft.DoesNotExist:
            return Response({"detail": "Aircraft not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AircraftAllSerializer(aircraft, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        })
class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightCreateSerializer

class CrewCreateView(generics.CreateAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewCreateSerializer

class AircraftCreateView(generics.CreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftAllSerializer

class ScheduleCreateView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class AirportCreateView(generics.CreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class TransitStopCreateView(generics.CreateAPIView):
    queryset = TransitStop.objects.all()
    serializer_class = TransitStopSerializer

class AircraftNumberListView(APIView):
    def get(self, request, *args, **kwargs):
        aircraft_numbers = Aircraft.objects.values_list('onBoard_number', flat=True)
        return Response({"onBoard_numbers": list(aircraft_numbers)})

class CrewListCreateView(generics.ListCreateAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewAllSerializer

    def perform_create(self, serializer):
        serializer.save()

class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()  # Получаем всех сотрудников
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

def AircraftModelListView(request):
    aircrafts = AircraftModel.objects.all()
    result = [f"{aircraft.manufacturer}-{aircraft.model_number}" for aircraft in aircrafts]
    return JsonResponse(result, safe=False)
def get_all_companies(request):
    companies = Airline.objects.values_list('company_name', flat=True)
    return JsonResponse(list(companies), safe=False)
def flight_count(request):
    count = Flight.objects.count()
    return JsonResponse({"count": count})

def aircraft_count(request):
    count = Aircraft.objects.count()
    return JsonResponse({"count": count})

def employee_count(request):
    count = Employee.objects.count()
    return JsonResponse({"count": count})

