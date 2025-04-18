#Importing the necessary modules
from rest_framework import serializers
from WorkerApi.models import Workers

#Creating a serializer class for the Workers model
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers  # ✔️ Correct
        fields = '__all__' #('w_id', 'w_name', 'w_email', 'w_phone', 'dtstamp')

