from measurement.views import ListSensorsAPIView, MeasurementAPIView, SensorAPIView
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('sensors/', ListSensorsAPIView.as_view()),
    path('measurements/', MeasurementAPIView.as_view()),
    path('sensors/<int:pk>/', SensorAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
