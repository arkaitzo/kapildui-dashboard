from django.shortcuts import render
from dashboard.models import *
from django.utils import timezone
from django.db.models import Avg
import math
from datetime import datetime

# Create your views here.
def dashboard_home(request):
    # Pedire al usuario un rango de maximo 6 horas
    start_date = datetime(2016,3,1,0,0,0) #16
    start_date = timezone.make_aware(start_date, timezone.get_current_timezone())
    end_date = datetime(2016,3,1,23,59,59) # 19,29,59
    end_date = timezone.make_aware(end_date, timezone.get_current_timezone())
    rango = [start_date,end_date]
    
    ##############################
    ########## RECEPTOR ##########
    ##############################
    # Tensiones DRX1
    drxpos5 = TensionesReceptor.objects.filter(fuente="drxpowpos5", fecha__range=rango).order_by('fecha'); #drxpos5 = drxpos5[::int(len(drxpos5)/144)]
    drxpos33 = TensionesReceptor.objects.filter(fuente="drxpowpos33", fecha__range=rango).order_by('fecha'); #drxpos33 = drxpos33[::int(len(drxpos33)/144)]
    drxneg5 = TensionesReceptor.objects.filter(fuente="drxpowneg5", fecha__range=rango).order_by('fecha'); #drxneg5 = drxneg5[::int(len(drxneg5)/144)]
    # Tensiones DRX2
    drx2pos5 = TensionesReceptor.objects.filter(fuente="drx1powpos5", fecha__range=rango).order_by('fecha'); #drx2pos5 = drx2pos5[::int(len(drx2pos5)/144)]
    drx2pos33 = TensionesReceptor.objects.filter(fuente="drx1powpos33", fecha__range=rango).order_by('fecha'); #drx2pos33 = drx2pos33[::int(len(drx2pos33)/144)]
    drx2neg5 = TensionesReceptor.objects.filter(fuente="drx1powneg5", fecha__range=rango).order_by('fecha'); #drx2neg5 = drx2neg5[::int(len(drx2neg5)/144)]
    # Temperaturas DRX1
    drxip = Temperaturas.objects.filter(sensor="drxtempifcal", fecha__range=rango).order_by('fecha'); #drxip = drxip[::int(len(drxip)/144)]
    drxdig = Temperaturas.objects.filter(sensor="drxtempdig", fecha__range=rango).order_by('fecha'); #drxdig = drxdig[::int(len(drxdig)/144)]
    drxana = Temperaturas.objects.filter(sensor="drxtempana", fecha__range=rango).order_by('fecha'); #drxana = drxana[::int(len(drxana)/144)]
    # Temperaturas DRX2
    drx2ip = Temperaturas.objects.filter(sensor="drx1tempifcal", fecha__range=rango).order_by('fecha'); #drx2ip = drx2ip[::int(len(drx2ip)/144)]
    drx2dig = Temperaturas.objects.filter(sensor="drx1tempdig", fecha__range=rango).order_by('fecha'); #drx2dig = drx2dig[::int(len(drx2dig)/144)]
    drx2ana = Temperaturas.objects.filter(sensor="drx1tempana", fecha__range=rango).order_by('fecha'); #drx2ana = drx2ana[::int(len(drx2ana)/144)]

    ##############################
    ######### TRANSMISOR #########
    ##############################
    # TX - Potencias Canales H y V
    poth = PotenciasTransmisor.objects.filter(canal="spbtxpowkw", fecha__range=rango, potencia__lt=140).order_by('fecha'); #poth = poth[::int(len(poth)/144)]
    potv = PotenciasTransmisor.objects.filter(canal="spbtxpowdpvkw", fecha__range=rango, potencia__gt=100).order_by('fecha'); #potv = potv[::int(len(potv)/144)]
    # Temperatura Sala Radar
    ecutemp = Temperaturas.objects.filter(sensor="ecupt100temp_1", fecha__range=rango).order_by('fecha'); #ecutemp = ecutemp[::int(len(ecutemp)/144)]
    # TX - Corriente del Solenoide
    solcurrent = CorrienteSolenoide.objects.filter(fecha__range=rango).order_by('fecha');
    # TX - Offset de potencia (entre ambos canales)
    offset = []
    horas_offset = []
    for i in range(len(poth)):
        for j in range(len(potv)):
            if poth[i].fecha == potv[j].fecha and potv[j].potencia != 0:
                horas_offset.append(poth[i].fecha)
                lineal = poth[i].potencia / potv[j].potencia
                offset.append(10*math.log(lineal,10))

    # Devolver las consultas realizadas
    return render(request, 'dashboard/bloques_radar.html', \
    	{'drxpos5':drxpos5, 'drxpos33':drxpos33, 'drxneg5':drxneg5, \
        'drx2pos5':drx2pos5, 'drx2pos33':drx2pos33, 'drx2neg5':drx2neg5, \
        'drxip':drxip, 'drxdig':drxdig, 'drxana':drxana, \
        'drx2ip':drx2ip, 'drx2dig':drx2dig, 'drx2ana':drx2ana, \
        'poth':poth, 'potv':potv, 'ecutemp':ecutemp, \
        'offset':zip(horas_offset,offset), \
        'solcurrent':solcurrent \
    	 } )
