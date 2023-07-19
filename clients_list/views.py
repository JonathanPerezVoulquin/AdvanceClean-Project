from django.shortcuts import render
from django.http import HttpResponse
from .models import clientList

# Create your views here.
def all_clients(request):
    clients = clientList.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})



def home_page(request):
    return  HttpResponse('Hello')