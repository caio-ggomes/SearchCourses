from django.shortcuts import render
from django.http import HttpResponse

from .models import Platform

# Create your views here.

def home(request):
    platforms = Platform.objects.all()
    return render(request, 'home.html', {'platforms': platforms})
