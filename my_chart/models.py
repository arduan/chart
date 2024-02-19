from datetime import datetime

from django.db import models
from django.db.models import Sum

GENDER_CHOICES = [
    ('муж','муж'),
    ('жен','жен'),
]

STATUS_CHOICES = [
    ('поступление','поступение'),
    ('перевод','перевод'),
     # Добавьте другие значения и метки, если нужно
]


class Chart(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    age = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    date_in = models.DateTimeField(null=True, blank=True)
    date_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, null=True, blank=True)
    sist_ad = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    diast_ad = models.DecimalField(max_digits=3, decimal_places=0, null=True)

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



