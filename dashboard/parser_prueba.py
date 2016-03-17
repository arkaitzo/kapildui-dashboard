from dashboard.models import *
from datetime import datetime,timedelta
from django.utils import timezone


# python manage.py shell
fecha = datetime(2016,3,1)
bite_path = './BITE/radar1_BITE' + fecha.strftime('%y%m%d') + '.log'
bite_hoy = open(bite_path, 'r')
lines_temp = bite_hoy.readlines()
bite_hoy.close()

# Eliminar lineas que no sean del dia en cuestion o del dia anterior
lines = []
for line in range(len(lines_temp)):
	if lines_temp[line][8:10] == fecha.strftime('%d') or lines_temp[line][8:10] == (fecha-timedelta(days=1)).strftime('%d'):
		lines.append(lines_temp[line])

# Media de cada diezminutal
choices_fuentes_rx = [ "drxpowpos5", "drxpowpos33", "drxpowneg5", "drx1powpos5", "drx1powpos33", "drx1powneg5" ]
choices_canales_tx = [ "spbtxpowkw", "spbtxpowdpvkw" ]
choices_temperaturas = [ "drxtempifcal", "drxtempdig", "drxtempana", "drx1tempifcal", "drx1tempdig", "drx1tempana", "ecupt100temp_1" ]
drxpowpos5 = {} # fecha,valor
for line in range(len(lines)):
	tag = lines[line].split('.')[0][21:]
	if tag in 'drxpowpos5':
		fechahora = datetime.strptime(lines[line][:19],"%Y-%m-%dT%H:%M:%S")
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		tension = float(lines[line].split('>')[-1][:-2])
		drxpowpos5[fechahora]=tension


date = drxpowpos5.keys()[0]
valor = drxpowpos5[a]

f = datetime(2016,2,29,22,0)



for line in range(len(lines)):
	tag = lines[line].split('.')[0][21:]
	if tag in choices_fuentes_rx:
		fechahora = datetime.strptime(lines[line][:19],"%Y-%m-%dT%H:%M:%S")
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		tension = float(lines[line].split('>')[-1][:-2])
		#TensionesReceptor.objects.create(fuente = tag, fecha = fechahora, tension = tension)
	elif tag in choices_canales_tx:
		fechahora = datetime.strptime(lines[line][:19],"%Y-%m-%dT%H:%M:%S")
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		potencia = float(lines[line].split('>')[-1][:-2])
		#PotenciasTransmisor.objects.create(canal = tag, fecha = fechahora, potencia = potencia)
	elif tag in choices_temperaturas:
		fechahora = datetime.strptime(lines[line][:19],"%Y-%m-%dT%H:%M:%S")
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		temperatura = float(lines[line].split('>')[-1][:-2])
		#Temperaturas.objects.create(sensor = tag, fecha = fechahora, temperatura = temperatura)
