from django.shortcuts import render

# Create your views here.
def all_clients(request):
    clients = clientList.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})
