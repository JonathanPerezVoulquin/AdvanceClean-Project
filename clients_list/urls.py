from django.urls import path

from . import views

urlpatterns = [
    path('clients/', views.all_clients, name='all clients'),
]