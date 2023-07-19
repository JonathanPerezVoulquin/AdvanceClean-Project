# Generated by Django 4.2.3 on 2023-07-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientList',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre_apellido', models.CharField(blank=True, db_column='Nombre_Apellido', max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=50, null=True)),
                ('ultimo_lavado', models.DateField(blank=True, db_column='Ultimo_lavado', null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=0, max_digits=50, null=True)),
                ('detalle', models.CharField(blank=True, db_column='Detalle', max_length=50, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=50, null=True)),
            ],
            options={
                'db_table': 'clients_list',
                'managed': True,
            },
        ),
    ]
