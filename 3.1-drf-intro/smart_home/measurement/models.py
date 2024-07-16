from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements',
        verbose_name='Датчик')
    temperature = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Значение')
    image = models.ImageField(
        upload_to='measurements',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата измерения')

    def __str__(self):
        return f"{self.sensor.name} - {self.value} - {self.date}"