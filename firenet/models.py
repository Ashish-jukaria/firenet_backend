from django.db import models

class Temperature(models.Model):
    temp=models.FloatField()

from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()  # Assuming temperature is a floating-point value
    humidity = models.FloatField()     # Assuming humidity is a floating-point value
    created_at = models.DateTimeField(auto_now_add=True)  # To keep track of when the data was created

    def __str__(self):
        return f"Temp: {self.temperature}, Humidity: {self.humidity}"



