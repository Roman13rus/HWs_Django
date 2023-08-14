from django.contrib import admin
from measurement.models import Measurement, Sensor

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass
# Register your models here.
