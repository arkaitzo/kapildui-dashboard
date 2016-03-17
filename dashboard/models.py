from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
choices_fuentes_rx = (
    ("drxpowpos5","DRX1 de +5.0V"), # drxpowpos5
    ("drxpowpos33","DRX1 de +3.3V"), # drxpowpos33
    ("drxpowneg5","DRX1 de -5.0V"), # drxpowneg5
    ("drx1powpos5","DRX2 de +5.0V"), # drx1powpos5
    ("drx1powpos33","DRX2 de +3.3V"), # drx1powpos33
    ("drx1powneg5","DRX2 de -5.0V"), # drx1powneg5
)

choices_canales_tx = (
    ("spbtxpowkw","Canal H"), # spbtxpowkw
    ("spbtxpowdpvkw","Canal V"), # spbtxpowdpvkw
)

choices_temperaturas = (
    ("drxtempifcal","DRX1 IP"), # drxtempifcal
    ("drxtempdig","DRX1 DIG"), # drxtempdig
    ("drxtempana","DRX1 ANA"), # drxtempana
    ("drx1tempifcal","DRX2 IP"), # drx1tempifcal
    ("drx1tempdig","DRX2 DIG"), # drx1tempdig
    ("drx1tempana","DRX2 ANA"), # drx1tempana
    ("ecupt100temp_1","ECU Sala Radar"), # ecupt100temp_1
)


class TensionesReceptor(models.Model):
    fuente = models.CharField(max_length = 12, choices=choices_fuentes_rx) # drx1powpos33
    fecha = models.DateTimeField(max_length=19) # 2016-03-01 12:00:25
    tension = models.DecimalField(max_digits=5, decimal_places=3) # xx.yyy

    def __unicode__(self): # __str__ en Python 3
        return self.fecha.strftime('%Y-%m-%d %H:%M:%S %Z')


class PotenciasTransmisor(models.Model):
    canal = models.CharField(max_length = 13, choices=choices_canales_tx) # spbtxpowdpvkw
    fecha = models.DateTimeField(max_length=19) # 2016-03-01 12:00:25
    potencia = models.DecimalField(max_digits=6, decimal_places=3) # xxx.yyy en kW

    def __unicode__(self): # __str__ en Python 3
        return self.fecha.strftime('%Y-%m-%d %H:%M:%S %Z')
    

class Temperaturas(models.Model):
    sensor = models.CharField(max_length = 14, choices=choices_temperaturas ) # ecupt100temp_1
    fecha = models.DateTimeField(max_length=19) # 2016-03-01 12:00:25
    temperatura = models.DecimalField(max_digits=5, decimal_places=3) # xx.yyy

    def __unicode__(self): # __str__ en Python 3
        return self.fecha.strftime('%Y-%m-%d %H:%M:%S %Z')

    
class CorrienteSolenoide(models.Model):
    fecha = models.DateTimeField(max_length=19) # 2016-03-01 12:00:25
    corriente = models.DecimalField(max_digits=5, decimal_places=3) # xx.yy en A

    def __unicode__(self): # __str__ en Python 3
        return self.fecha.strftime('%Y-%m-%d %H:%M:%S %Z')



"""
def publish(self):
    self.published_date = timezone.now()
    self.save()
"""
