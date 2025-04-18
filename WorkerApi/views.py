#Imports 
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Workers
from .serializers import WorkerSerializer

# Create your views here.
class addWorkerView(viewsets.ModelViewSet):
    queryset = Workers.objects.all() #.order_by('-dtstamp')
    serializer_class = WorkerSerializer

# Function-based view to get Worker data by ID
def get_worker_by_id(request, id):
    worker = get_object_or_404(Workers, pk=id)
    return render(request, 'worker_detail.html', {'worker': worker})