from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

from . import forms


def home(request):
    return render(request, "Home/index.html")

#! LOGIN


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/index.html", {"mensaje": "Inició sesión correctamente"})

    else:
        form = forms.CustomAuthenticationForm
        return render(request, "Home/login.html", {"form": form})

#! SIGNUP


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "Home/index.html", {"mensaje": "La cuenta se creó correctamente"})

    else:
        form = forms.CustomUserCreationForm()
        return render(request, "Home/register.html", {"form": form})
