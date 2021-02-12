from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "sala/home.html")

def listadogeneralsalas(request):
    return render(request, "sala/listadogeneralsalas.html")

def detalledeunasala(request):
    return render(request, "sala/detalledeunasala.html")

def resultadopeliculasexhibidas(request):
    return render(request, "sala/resultadopeliculasexhibidas.html")