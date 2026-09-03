from .models import Sensor, Measurement
from .serializers import (
    MeasurementSerializer,
    MeasurementCreateSerializer,
    SensorSerializer,
    SensorDetailSerializer
)
from rest_framework import viewsets, generics

class SensorCreateView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class SensorUpdateView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer
    
    
class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class SensorDetailView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
