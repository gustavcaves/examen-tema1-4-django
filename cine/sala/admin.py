from django.contrib import admin
from .models import Peliculas, programacionSala, Sala

# Register your models here.


class programacionSalaAdmin(admin.ModelAdmin):
    list_display = ('datee', 'hour', 'movie')
    readonly_fields = ('created', 'updated')
    search_fields = ('movie',)
    date_hierarchy = ('datee')
    list_filter = ('datee',)

class programacionSalaInline(admin.TabularInline):
    list_display = ('datee', 'hour', 'movie')
    readonly_fields = ('created', 'updated')
    search_fields = ('movie',)
    date_hierarchy = ('datee')
    list_filter = ('datee',)
    model = programacionSala
    extra = 2

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year')
    readonly_fields = ('created', 'updated')
    search_fields = ('title',)
    date_hierarchy = ('year')
    list_filter = ('year',)
    inlines = [programacionSalaInline]
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'description', 'year')
    #     }),
    # )

class SalaAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_chair','created', 'updated')
    readonly_fields = ('created', 'updated')
    search_fields = ('name',)
    date_hierarchy = ('created')
    list_filter = ('name',)

admin.site.register(Peliculas, PeliculasAdmin)
admin.site.register(programacionSala, programacionSalaAdmin)
admin.site.register(Sala, SalaAdmin)