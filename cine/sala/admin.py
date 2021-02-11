from django.contrib import admin
from .models import Peliculas, programacionSala

# Register your models here.

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year')
    readonly_fields = ('created', 'updated')

class programacionSalaAdmin(admin.ModelAdmin):
    list_display = ('datee', 'hour', 'movie')
    readonly_fields = ('created', 'updated')

admin.site.register(Peliculas, PeliculasAdmin)
admin.site.register(programacionSala, programacionSalaAdmin)