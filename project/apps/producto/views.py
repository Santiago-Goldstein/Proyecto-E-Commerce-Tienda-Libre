from typing import Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


@login_required
def index(request):
    return render(request, "producto/index.html")


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria


class ProductoCategoriaCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    permission_required = 'producto.add_categoriadeproductos'


class ProductoCategoriaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    permission_required = 'producto.change_categoriadeproductos'


class ProductoCategoriaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    permission_required = 'producto.delete_categoriadeproductos'


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
