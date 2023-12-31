# Generated by Django 4.2.6 on 2023-11-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_owner', models.CharField(max_length=255)),
                ('lastname_owner', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('name_pet_id', models.IntegerField()),
                ('name_pet_real', models.CharField(max_length=255)),
                ('race_pet', models.CharField(max_length=255)),
                ('gender_pet', models.CharField(max_length=10)),
                ('color_pet', models.CharField(max_length=50)),
                ('species_pet', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('state_appointment', models.IntegerField()),
                ('service_id', models.IntegerField()),
                ('date_appointment', models.DateField()),
                ('hour_appointment', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pet', models.CharField(max_length=255)),
                ('gender_pet', models.CharField(max_length=10)),
                ('weight_pet', models.DecimalField(decimal_places=2, max_digits=5)),
                ('species_pet', models.CharField(max_length=50)),
                ('age_pet', models.IntegerField()),
                ('sterilize_pet', models.BooleanField()),
                ('race_pet', models.CharField(max_length=50)),
                ('color_pet', models.CharField(max_length=50)),
                ('medicine_preventive', models.TextField()),
                ('name_owner', models.CharField(max_length=255)),
                ('tel_owner', models.CharField(max_length=20)),
                ('address_owner', models.CharField(max_length=255)),
                ('fc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fr', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fill_capillary', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pulse', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diagnosis_differential', models.TextField()),
                ('diagnosis_final', models.TextField()),
                ('test_laboratory', models.TextField()),
                ('treatment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_pet', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('race', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('species', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('color', models.CharField(max_length=50)),
                ('asset', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=50)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='productos/')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_service', models.AutoField(primary_key=True, serialize=False)),
                ('name_service', models.CharField(max_length=255)),
                ('description_service', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
