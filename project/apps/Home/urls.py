from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_request, name="login"),
    path("about/", TemplateView.as_view(template_name="Home/about.html"), name="about"),
]


urlpatterns += staticfiles_urlpatterns()
