from django.urls import path
from . import views

appname = "main"

urlpatterns = [
    path('login/', views.login_page, name="login")
]