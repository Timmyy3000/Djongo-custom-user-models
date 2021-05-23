from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

appname = "main"

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout")
    
]