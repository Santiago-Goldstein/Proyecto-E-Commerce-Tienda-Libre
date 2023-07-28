from typing import Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models
from .models import Producto, ProductoCategoria


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


class ProductoList(ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = ProductoCategoria.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            categoria = ProductoCategoria.objects.get(id=categoria_id)
            queryset = queryset.filter(categoria=categoria)
        return queryset


class ProductoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # CREAR
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")
    permission_required = 'producto.change_producto'


class ProductoDetail(DetailView):  # DETAIL
    model = models.Producto


class ProductoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # UPDATE
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")
    permission_required = 'producto.change_producto'


class ProductoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # DELETE
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    permission_required = 'producto.delete_producto'
