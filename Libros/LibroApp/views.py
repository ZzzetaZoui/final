from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader, context, Template
from LibroApp.models import *

def inicio(request):
    return render(request, 'LibroApp/inicio.html')
