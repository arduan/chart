from datetime import datetime, timedelta
from urllib import request

from django.http import HttpResponse
from django.urls.base import reverse

from .models import Chart
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, TemplateView, DetailView


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest"] = Chart.objects.all().order_by("-date_in")[:100]
        context["count"] = Chart.objects.all().count()
        result = context["count"] / 10 * 100  # Например, умножение на 100
        context["result"] = result  # Добавляем результат вычислений в контекст

        # Получаем текущую дату и время
        current_datetime = datetime.now()
        # Определяем дату и время 24 часа назад от текущего момента
        twenty_four_hours_ago = current_datetime - timedelta(hours=24)
        # Фильтруем объекты по дате и времени поступления за последние 24 часа
        patients_last_24_hours = Chart.objects.filter(date_in__range=(twenty_four_hours_ago, current_datetime)).count()
        context["patients_last_24_hours"] = patients_last_24_hours

        return context


class YourDetailView(DetailView):
    model = Chart
    template_name = 'hello.html'
    context_object_name = 'object'
    slug_field = 'slug'
