from django.http import response
from django.shortcuts import render

# Create your views here.

def index(response) :
    return render(response, 'main/home.html')