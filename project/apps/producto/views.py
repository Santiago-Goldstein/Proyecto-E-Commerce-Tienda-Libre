from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


def index(request):
    return render(request, "producto/index.html")


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
