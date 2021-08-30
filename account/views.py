from django import forms
from django.shortcuts import redirect, render
from .forms import login_form, register_form
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    form_login = login_form(request.POST or None)
    if form_login.is_valid():
        username = form_login.cleaned_data.get("username")
        password = form_login.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            form_login.add_error('username', 'username or password is not valid')

    context = {
        "form_login": form_login,
    }
    return render(request, "login.html", context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form_register = register_form(request.POST or None)
    if form_register.is_valid():
        username = form_register.cleaned_data.get("username")
        email = form_register.cleaned_data.get("email")
        password = form_register.cleaned_data.get("password")
        User.objects.create_user(username=username, email=email, password=password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")

    context = {
        "form_register": form_register
    }
    return render(request, 'register.html', context)


def logout_Page(request):
    logout(request)
    return redirect('/login')