from django.urls import path
from . import views

urlpatterns = [
    path('listadogeneralsalas/', views.listadogeneralsalas, name='listadogeneralsalas'),
    path('detalledeunasala/<id>', views.detalledeunasala, name='detalledeunasala'),
    path('resultadopeliculasexhibidas/<sala>', views.resultadopeliculasexhibidas, name='resultadopeliculasexhibidas'),
    path('', views.home, name='home'),
]