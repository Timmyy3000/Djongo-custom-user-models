from django.http import response
from django.shortcuts import render

# Create your views here.

def dashboard(response) :
    return render(response, 'main/dashboard.html')