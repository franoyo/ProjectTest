from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, Permission, Group
class CustomUser(AbstractUser):
    name = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento =  models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=30)

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    def __str__(self):
        return self.username


class Cita(models.Model):
    name_owner = models.CharField(max_length=255)
    lastname_owner = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    document = models.CharField(max_length=20)
    email = models.EmailField()
    name_pet_id = models.IntegerField()
    name_pet_real = models.CharField(max_length=255)
    color_pet = models.CharField(max_length=50)
    date_birth = models.DateField()
    state_appointment = models.IntegerField()
    service_id = models.IntegerField()
    date_appointment = models.DateField()
    hour_appointment = models.TimeField()

    def __str__(self):
        return f"{self.name_owner} - {self.name_pet_real}"

    class meta:
        verbose_name = "Cita"
        verbose_name_plural = "citas"
        db_table = "Citas"
        ordering = ["service_id"]


class EstadoCita(models.Model):
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.state

    class meta:
        verbose_name = "EstadoCita"
        verbose_name_plural = "estadosCitas"
        db_table = "EstadosCitas"
        ordering = ["state"]


class HistoriaClinica(models.Model):
    name_pet = models.CharField(max_length=255)
    weight_pet = models.DecimalField(max_digits=5, decimal_places=2)
    age_pet = models.IntegerField()
    sterilize_pet = models.BooleanField()
    color_pet = models.CharField(max_length=50)
    medicine_preventive = models.TextField()
    name_owner = models.CharField(max_length=255)
    tel_owner = models.CharField(max_length=20)
    address_owner = models.CharField(max_length=255)
    fc = models.DecimalField(max_digits=5, decimal_places=2)
    fr = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    fill_capillary = models.DecimalField(max_digits=5, decimal_places=2)
    pulse = models.DecimalField(max_digits=5, decimal_places=2)
    diagnosis_differential = models.TextField()
    diagnosis_final = models.TextField()
    test_laboratory = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return self.name_pet

    class meta:
        verbose_name = "HistoriaClinica"
        verbose_name_plural = "historiasClinicas"
        db_table = "HistoriasClinicas"
        ordering = ["name_pet"]


class Mascota(models.Model):
    id_pet = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    date_birth = models.DateField()
    color = models.CharField(max_length=50)
    asset = models.BooleanField()

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "Mascota"
        verbose_name_plural = "mascotas"
        db_table = "Mascotas"
        ordering = ["id_pet"]


class Producto(models.Model):
    id_product = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    brand = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    location = models.DateField()
    image = models.ImageField(upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return self.description

    class meta:
        verbose_name = "Producto"
        verbose_name_plural = "productos"
        db_table = "ProductoS"
        ordering = ["id_product"]


class Servicio(models.Model):
    id_service = models.AutoField(primary_key=True)
    name_service = models.CharField(max_length=255)
    description_service = models.TextField()

    def __str__(self):
        return self.name_service

    class meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        db_table = "Servicios"
        ordering = ["name_service"]


class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
