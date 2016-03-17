from django.contrib import admin
from .models import *

class TensionesReceptorAdmin(admin.ModelAdmin):
    list_display = ('fuente', 'fecha', 'tension',)
    list_filter = ('fuente','fecha',)

class PotenciasTransmisorAdmin(admin.ModelAdmin):
    list_display = ('canal', 'fecha', 'potencia',)
    list_filter = ('canal','fecha',)

class TemperaturasAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'fecha', 'temperatura',)
    list_filter = ('sensor','fecha',)

class CorrienteSolenoideAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'corriente',)


# Register your models here.
admin.site.register(TensionesReceptor, TensionesReceptorAdmin)
admin.site.register(PotenciasTransmisor, PotenciasTransmisorAdmin)
admin.site.register(Temperaturas, TemperaturasAdmin)
admin.site.register(CorrienteSolenoide, CorrienteSolenoideAdmin)
