from .models import Booking, Flight
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from .serializers import ListFlightSerial, ListBookingSerial,flightCreateSerializer,BookingDetailSerializer



class FlightList_API_View(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListFlightSerial
    

class BookingList_API_View(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = ListBookingSerial
    

class FlightList_detail_View(RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListFlightSerial
    lookup_field = "id"
    lookup_url_kwarg = "flight_id"

class Booking_detail_View(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"



class flight_create_view(CreateAPIView):
    serializer_class = flightCreateSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


