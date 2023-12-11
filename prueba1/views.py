
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser  # Asegúrate de importar tu modelo CustomUser

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        apellido = request.POST['apellido']
        documento = request.POST['documento']
        direccion = request.POST['direccion']
        celular = request.POST['celular']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password == password_confirmation:
            # Verifica si el usuario ya existe
            if CustomUser.objects.filter(username=email).exists():
                messages.error(request, 'Ya existe un usuario con este correo electrónico.')
            else:
                # Crear el objeto CustomUser y guardarlo en la base de datos
                user = CustomUser.objects.create_user(username=email, email=email,password=password)
                user.name = name
                user.apellido = apellido
                user.documento = documento
                user.direccion = direccion
                user.celular = celular
                user.save()
                return redirect('autenticacion:registroExitoso')  # Puedes redirigir a la página de inicio de sesión o a donde desee
        else:
            messages.error(request, 'Las contraseñas no coinciden. Intenta nuevamente.')

    return render(request, 'Auth/registrarse.html')

def alertSucess(request):
    return render(request,'alertas/registro_exitoso.html',{
        #context
    })