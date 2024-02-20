from django.contrib import admin
from django.urls import path

from my_chart.views import HomePageView, YourDetailView


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("hello/<slug:slug>", YourDetailView.as_view(), name="hello"),

]




