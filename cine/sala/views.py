from django.shortcuts import render
from .models import Sala

# Create your views here.

def home(request):
    return render(request, "sala/home.html")

def listadogeneralsalas(request):
    lgeneralsalas = Sala.objects.all()
    return render(request, "sala/listadogeneralsalas.html", {'lgeneralsalas':lgeneralsalas})

def detalledeunasala(request):
    return render(request, "sala/detalledeunasala.html")

def resultadopeliculasexhibidas(request):
    return render(request, "sala/resultadopeliculasexhibidas.html")