from rest_framework import serializers
from .models import Flight,Booking

class ListFlightSerial(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        fields = ['id' , 'destination','time','price']
        
class ListBookingSerial(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        fields = ['id','flight' , 'date']



class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "flight", "date", "passengers"]       

class flightCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id' , 'destination','time','price']


