from django.shortcuts import render
from .models import Sala, programacionSala

# Create your views here.

def home(request):
    return render(request, "sala/home.html")

def listadogeneralsalas(request):
    lgeneralsalas = Sala.objects.all()
    return render(request, "sala/listadogeneralsalas.html", {'lgeneralsalas':lgeneralsalas} )

def detalledeunasala(request, sala):
    lprograma = programacionSala.objects.get(sala=sala)
    return render(request, "sala/detalledeunasala.html", {'lprograma':lprograma})

def resultadopeliculasexhibidas(request):
    return render(request, "sala/resultadopeliculasexhibidas.html")