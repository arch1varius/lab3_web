from rest_framework import serializers
from .models import Client, Ticket, Flight, Crew, Aircraft, Schedule, Airport, TransitStop, Employee, AircraftModel, \
    Airline


# Serializer для Клиента и Билетов
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(source='ticket_set', many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['passenger_data', 'full_name', 'phone_number', 'tickets']

class TransitStopSerializer(serializers.ModelSerializer):
    airport_arrival_address = serializers.CharField(source='airport_number.address')

    class Meta:
        model = TransitStop
        fields = ['airport_arrival_address']  # Только адрес прибытия теперь


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['company_name']  # Только имя компании

class AircraftModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftModel
        fields = '__all__'
class AircraftAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'
class AircraftSerializer(serializers.ModelSerializer):
    model_details = AircraftModelSerializer(source='model_number')
    company_name = AirlineSerializer()

    class Meta:
        model = Aircraft
        fields = [
            'onBoard_number',
            'company_name',
            'flight_hours',
            'last_maintenance_date',
            'manufacture_date',
            'model_details',
        ]
class FlightSerializerStandart(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    airport = AirportSerializer(source='airport_number', read_only=True)
    transit_stops = TransitStopSerializer(source='transitstop_set', many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = ['schedule_number', 'departure_time', 'arrival_time', 'airport', 'transit_stops']

class CrewSerializer(serializers.ModelSerializer):
    employee_code = serializers.IntegerField(source='employee_code.employee_code')  # employee_code — это внешний ключ, возвращаем employee_code из Employee

    class Meta:
        model = Crew
        fields = ['employee_code']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_code', 'full_name']

class CrewAllSerializer(serializers.ModelSerializer):
    employee_code = EmployeeSerializer(read_only=True)  # Используем вложенный сериализатор

    class Meta:
        model = Crew
        fields = '__all__'

class CrewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ['medical_check_date', 'clearance_status', 'flight_position', 'flight_number', 'employee_code']

# Сериализатор для рейса
class FlightSerializer(serializers.ModelSerializer):
    crew = CrewSerializer(source='crew_set', many=True, read_only=True)
    aircraft = AircraftSerializer(source='onBoard_number', read_only=True)
    schedule = serializers.StringRelatedField(source='schedule_number')
    transit_stops = TransitStopSerializer(source='schedule_number.transitstop_set', many=True, read_only=True)
    airport_departure_address = serializers.CharField(source='schedule_number.airport_number.address')  # Берем адрес аэропорта вылета из schedule

    class Meta:
        model = Flight
        fields = [
            'flight_number',
            'departure_date',
            'arrival_date',
            'status',
            'aircraft',
            'crew',
            'schedule',
            'transit_stops',
            'airport_departure_address',  # Добавляем сюда адрес
        ]

class AircraftNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['onBoard_number']

class FlightCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['onBoard_number', 'schedule_number', 'departure_date', 'arrival_date', 'status']

    def create(self, validated_data):
        flight = Flight.objects.create(**validated_data)
        return flight
