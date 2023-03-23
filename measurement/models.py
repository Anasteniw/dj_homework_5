from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description=models.CharField(max_length=150, verbose_name='Описание')

class Measurement(models.Model):
    sensors=models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature=models.DecimalField(max_digits=3, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата/время измерения')