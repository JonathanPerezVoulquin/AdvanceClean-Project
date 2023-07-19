from django.contrib import admin

from .models import clientList
# Register your models here.
class Client(admin.ModelAdmin):
    list_display = ('id', 'nombre_apellido', 'direccion', 'telefono','ultimo_lavado','precio','detalle','email')
    class Meta:
        managed = False
        db_table = 'clients_list'



admin.site.register(clientList,Client)