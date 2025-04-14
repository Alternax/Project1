
#Imports 
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Vehicle
from .serializer import VehicleSerializer

# Create your views here.
class addVehicleView(viewsets.ModelViewSet):

    queryset = Vehicle.objects.all() #.order_by('-dtstamp')
    serializer_class = VehicleSerializer

# Function-based view to get Vehicle data by ID
def get_vehicle_by_id(request, id):
    vehicle = get_object_or_404(Vehicle, pk=id)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})
