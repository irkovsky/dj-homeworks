from django.urls import path
from .views import (
    SensorCreateView, SensorDetailView,
    SensorUpdateView, SensorListView,
    MeasurementCreateView
)

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/<int:pk>', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensors/', SensorCreateView.as_view(), name='sensor-create'),
    path('sensors/<int:pk>', SensorUpdateView.as_view(), name='sensor-update'),
    
    path('measurement/', MeasurementCreateView.as_view(), name='measurement-create')
]
