from django.contrib import admin
from .models import Peliculas

# Register your models here.

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year')
    readonly_fields = ('created', 'updated')

admin.site.register(Peliculas, PeliculasAdmin)