from django.shortcuts import render
from .models import Sala, programacionSala

# Create your views here.

def home(request):
    return render(request, "sala/home.html")

def listadogeneralsalas(request):
    lgeneralsalas = Sala.objects.all()
    return render(request, "sala/listadogeneralsalas.html", {'lgeneralsalas':lgeneralsalas} )

def detalledeunasala(request, id):
    lgeneralsalas = Sala.objects.get(id=id)
    return render(request, "sala/detalledeunasala.html", {'lgeneralsalas':lgeneralsalas} )

def resultadopeliculasexhibidas(request, sala):
    lprograma = programacionSala.objects.filter(sala=sala)
    return render(request, "sala/resultadopeliculasexhibidas.html", {'lprograma':lprograma})