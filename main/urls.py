from django.urls import path
from . import views

appname = "main"

urlpatterns = [
    path('dashboard/', views.dashboard, {})
]