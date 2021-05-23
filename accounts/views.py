from accounts.forms import LoginForm, RegisterForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from django import forms

def login_page(response):
    form = LoginForm(response.POST or None)

    context = {'form' : form}

    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(response, username=username, password=password)
        if user is not None:
           
            login(response, user)
            context = {"form" : form, "user": user}

            return redirect("/dashboard")

    else:

        print("error, wrong email")
        forms.ValidationError("Wrong Password")
        
    
    

    return render(response, "accounts/login.html", context)


def register(response):
    
    if response.method == "POST":
       
        form = RegisterForm(response.POST or None)
        context = {
            "form" : form
        }

        if form.is_valid():
            user = form.save()
            context = {
            "form" : form,
            "user" : user
        }
            return redirect('/login/')

    else:
        form = RegisterForm()
    return render(response, 'accounts/register.html', {"form":form})


def logout_view (response):
    logout(response)

    return redirect('/login')


