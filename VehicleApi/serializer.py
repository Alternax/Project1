
from rest_framework import serializers
from VehicleApi.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle  # ✔️ Correct
        fields = '__all__' #('v_id', 'v_regnNo', 'v_model', 'v_make', 'dtstamp')
