from accounts.forms import LoginForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url



def login_page (response):
    form = LoginForm(response.POST or None)

    context = { "form" : form}

    if form.is_valid ():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(response, username = username, password = password)
        if user is not None :
            login(response, user)

            try :
                pass
            except:
                pass
            
            return redirect("/home")
    
    else :

        print("error")

    return render (response, "accounts/login.html", context)

    