from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Cita, HistoriaClinica, Mascota, Producto, EstadoCita, Servicio, Raza, CustomUser

# Define un recurso para cada modelo que deseas exportar
class CitaResource(resources.ModelResource):
    class Meta:
        model = Cita

class HistoriaClinicaResource(resources.ModelResource):
    class Meta:
        model = HistoriaClinica

class MascotaResource(resources.ModelResource):
    class Meta:
        model = Mascota

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class EstadoCitaResource(resources.ModelResource):
    class Meta:
        model = EstadoCita

class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio

class RazaResource(resources.ModelResource):
    class Meta:
        model = Raza

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

# Registra tus modelos utilizando ImportExportModelAdmin
@admin.register(Cita)
class CitaAdmin(ImportExportModelAdmin):
    resource_class = CitaResource

@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(ImportExportModelAdmin):
    resource_class = HistoriaClinicaResource

@admin.register(Mascota)
class MascotaAdmin(ImportExportModelAdmin):
    resource_class = MascotaResource

@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource

@admin.register(EstadoCita)
class EstadoCitaAdmin(ImportExportModelAdmin):
    resource_class = EstadoCitaResource

@admin.register(Servicio)
class ServicioAdmin(ImportExportModelAdmin):
    resource_class = ServicioResource

@admin.register(Raza)
class RazaAdmin(ImportExportModelAdmin):
    resource_class = RazaResource

@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource
