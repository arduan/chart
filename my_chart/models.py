from datetime import datetime

from django.db import models
from django.db.models import Sum

YOUR_CHOICES = [
    ('gender1', 'муж'), ('gender2', 'жен'),
    # Добавьте другие значения и метки, если нужно
]


class Chart(models.Model):
    name = models.CharField(max_length=30)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    gender = models.CharField(max_length=3)
    date_in = models.DateTimeField()
    sist_ad = models.DecimalField(max_digits=3, decimal_places=0)
    diast_ad = models.DecimalField(max_digits=3, decimal_places=0)

    @property
    def avrg_ad(self):
        # Вычисляем среднее (перфузионное) артериальное давление пациента
        return (self.sist_ad + self.diast_ad * 2) / 3

    @property
    def delta_puls(self):
        # Вычиление пульсового давления
        return self.sist_ad - self.diast_ad

    @property
    def all_count(self):
        my_count = models.IntegerField(default=Chart.objects().aggregate(Sum('count'))['count'])
        return my_count


    def __str__(self):
        return self.name



