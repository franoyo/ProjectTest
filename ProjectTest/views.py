
from django.shortcuts import render
def index(request):
    return render(request,'index.html',{
        #context
    })

def info(request):
    return render(request,'info.html',{
        #context
    })
def conocenos(request):
    return render(request,'conocenos.html',{
        #context
    })
def servicios(request):
    return render(request,'servicios.html',{
        #context
    })
def spa(request):
    return render(request,'spa.html',{
        #context
    })
def consulta(request):
    return render(request,'consulta.html',{
        #context
    })
def viaje(request):
    return render(request,'viaje.html',{
        #context
    })
def guarderia(request):
    return render(request,'guarderia.html',{
        #context
    })
def login(request):
    return render(request,'login.html',{
        #context
    })
def registro(request):
    return render(request,'registrarse.html',{
        #context
    })