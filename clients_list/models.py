from django.db import models

# Create your models here.
class clientList(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_apellido = models.CharField(db_column='Nombre_Apellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ultimo_lavado = models.DateField(db_column='Ultimo_lavado', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    detalle = models.CharField(db_column='Detalle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apodo = models.CharField(db_column='Apodo', max_length=40)

    class Meta:
        managed = False
        db_table = 'clients_list'
