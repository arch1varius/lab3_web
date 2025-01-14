# Generated by Django 5.1.3 on 2024-12-01 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0002_alter_drivelicense_id_owner_alter_ownership_id_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftModel',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=20)),
                ('number_of_seats', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('purpose', models.CharField(max_length=50)),
                ('fuel_consumption', models.IntegerField()),
                ('payload_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('number_of_employees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('number_of_runways', models.IntegerField()),
                ('number_of_transits', models.IntegerField()),
                ('lounge_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('passenger_data', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='ownership',
            name='id_owner',
        ),
        migrations.RemoveField(
            model_name='drivelicense',
            name='id_owner',
        ),
        migrations.RemoveField(
            model_name='ownership',
            name='id_vehicle',
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('onBoard_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('flight_hours', models.IntegerField()),
                ('last_maintenance_date', models.DateField()),
                ('manufacture_date', models.DateField()),
                ('model_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.aircraftmodel')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.airline')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_code', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('flight_hours', models.IntegerField()),
                ('position', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('company_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab3.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_number', models.IntegerField(primary_key=True, serialize=False)),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('onBoard_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('crew_number', models.IntegerField(primary_key=True, serialize=False)),
                ('medical_check_date', models.DateField()),
                ('clearance_status', models.IntegerField()),
                ('flight_position', models.CharField(max_length=30)),
                ('employee_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.employee')),
                ('flight_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_number', models.IntegerField(primary_key=True, serialize=False)),
                ('total_flight_time_hours', models.IntegerField()),
                ('periodicity', models.IntegerField()),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('airport_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.airport')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='schedule_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.schedule'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_number', models.IntegerField(primary_key=True, serialize=False)),
                ('seat_type', models.CharField(max_length=20)),
                ('boarding_number', models.IntegerField()),
                ('payment_type', models.CharField(max_length=20)),
                ('registration_status', models.CharField(max_length=20)),
                ('flight_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.flight')),
                ('passenger_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.client')),
            ],
        ),
        migrations.CreateModel(
            name='TransitStop',
            fields=[
                ('transit_number', models.IntegerField(primary_key=True, serialize=False)),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('time_in_airport_minutes', models.IntegerField()),
                ('airport_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.airport')),
                ('schedule_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3.schedule')),
            ],
        ),
        migrations.DeleteModel(
            name='CarOwner',
        ),
        migrations.DeleteModel(
            name='DriveLicense',
        ),
        migrations.DeleteModel(
            name='Ownership',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]