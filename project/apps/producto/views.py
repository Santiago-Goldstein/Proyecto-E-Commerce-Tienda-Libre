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

###########################
##   ProductoCategoria   ##
###########################


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

###########################
##       Producto        ##
###########################


class ProductoList(ListView):  # LIST
    model = models.Producto

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(
                nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list


class ProductoCreate(CreateView):  # CREAR
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetail(DetailView):  # DETAIL
    model = models.Producto


class ProductoUpdate(UpdateView):  # UPDATE
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDelete(DeleteView):  # DELETE
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
