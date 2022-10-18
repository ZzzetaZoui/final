from django.urls import path
from LibroApp.views import *


urlpatterns = [
    path('inicio/', inicio, name="inicio"),
]