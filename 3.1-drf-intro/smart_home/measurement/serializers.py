from rest_framework import serializers
from .models import Sensor, Measurement    
        
class MeasurementSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
        

class MeasurementCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'image']