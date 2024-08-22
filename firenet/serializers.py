from .models import * 

from rest_framework import serializers


class Temperature_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Temperature
        fields = '__all__'

from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature', 'humidity', 'created_at']
