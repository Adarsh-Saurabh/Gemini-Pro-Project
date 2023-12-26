from django.urls import path
from . import views

urlpatterns = [
    path('', views.page),
    path('generate', views.generate)]