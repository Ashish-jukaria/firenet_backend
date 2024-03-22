from .models import * 

from rest_framework import serializers


class Temperature_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Temperature
        fields = '__all__'
