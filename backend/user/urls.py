from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='Register'),
]
