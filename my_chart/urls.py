from django.contrib import admin
from django.urls import path, include

from my_chart.views import HomePageView, PatientPageView
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("hello/", PatientPageView.as_view(), name="hello"),

]




