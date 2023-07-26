from django.contrib import admin

from .models import clientList
# Register your models here.
class Client(admin.ModelAdmin):
    list_display = ('id', 'nombre_apellido', 'direccion', 'telefono', 'ultimo_lavado', 'precio', 'detalle', 'email')
    list_editable = ('nombre_apellido', 'direccion', 'telefono', 'ultimo_lavado', 'precio', 'detalle', 'email')
    search_fields = ['nombre_apellido', 'direccion', 'telefono']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term.strip():
            # Si se proporciona un término de búsqueda, buscamos coincidencias en nombre o dirección
            queryset |= self.model.objects.filter(nombre_apellido__icontains=search_term) | self.model.objects.filter(direccion__icontains=search_term)
        return queryset, use_distinct

    def save_model(self, request, obj, form, change):
        # Buscamos un cliente existente por dirección o nombre o telefono 
        existing_client = clientList.objects.filter(direccion=obj.direccion).first()
        if not existing_client:
            existing_client = clientList.objects.filter(nombre_apellido=obj.nombre_apellido).first()
        if not existing_client:
            existing_client = clientList.objects.filter(telefono=obj.telefono).first()

        if existing_client:
            # Si encontramos un cliente existente, actualizamos el campo 'ultimo_lavado' y el 'precio'
            existing_client.ultimo_lavado = obj.ultimo_lavado
            existing_client.precio = obj.precio
            existing_client.save()
            obj.pk = existing_client.pk  # Establecemos el ID del cliente existente en el objeto actual
        else:
            # Si no encontramos un cliente existente, se crea un nuevo cliente con los campos completados
            obj.save()


class Meta:
    managed = True
    db_table = 'clients_list'


admin.site.register(clientList,Client)