from django.urls import path
from . import views

urlpatterns = [
    path('listadogeneralsalas/', views.listadogeneralsalas, name='listadogeneralsalas'),
    path('detalledeunasala/', views.detalledeunasala, name='detalledeunasala'),
    path('resultadopeliculasexhibidas/', views.resultadopeliculasexhibidas, name='resultadopeliculasexhibidas'),
    path('', views.home, name='home'),
]