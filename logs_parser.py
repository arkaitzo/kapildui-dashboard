from dashboard.models import *
from datetime import datetime
from django.utils import timezone
from django.db.models import Avg
import time

tic = time.time()

bite_path = './BITE/radar1_BITE160301.log'
bite_hoy = open(bite_path, 'r')
lines = bite_hoy.readlines()
bite_hoy.close()


choices_fuentes_rx = [ "drxpowpos5", "drxpowpos33", "drxpowneg5", "drx1powpos5", "drx1powpos33", "drx1powneg5" ]
item = 0
while item < len(choices_fuentes_rx):
	for line in range(len(lines)):
		tag = lines[line].split('.')[0][21:]
		if tag == choices_fuentes_rx[item]:
			fechahora = datetime.strptime(lines[line][:16],"%Y-%m-%dT%H:%M")
			fechahora = fechahora.replace(minute = ((fechahora.minute/10)*10))
			fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
			valor = float(lines[line].split('>')[-1][:-2])
			TempDB.objects.create(tag = tag, fecha = fechahora, valor = valor)
	valores = TempDB.objects.filter(tag=choices_fuentes_rx[item]).values('fecha').annotate(avg=Avg('valor'))
	for j in range(len(valores)):
		TensionesReceptor.objects.create(fuente = choices_fuentes_rx[item], fecha = valores[j]['fecha'], tension = valores[j]['avg'])
	TempDB.objects.all().delete()
	item += 1
#TempDB.objects.all().delete() # Borrar todo de TempDB

choices_canales_tx = [ "spbtxpowkw", "spbtxpowdpvkw" ]
item = 0
while item < len(choices_canales_tx):
	for line in range(len(lines)):
		tag = lines[line].split('.')[0][21:]
		if tag == choices_canales_tx[item]:
			fechahora = datetime.strptime(lines[line][:16],"%Y-%m-%dT%H:%M")
			fechahora = fechahora.replace(minute = ((fechahora.minute/10)*10))
			fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
			valor = float(lines[line].split('>')[-1][:-2])
			if valor > 100 and valor < 140:
				TempDB.objects.create(tag = tag, fecha = fechahora, valor = valor)
	valores = TempDB.objects.filter(tag=choices_canales_tx[item]).values('fecha').annotate(avg=Avg('valor'))
	for j in range(len(valores)):
		PotenciasTransmisor.objects.create(canal = choices_canales_tx[item], fecha = valores[j]['fecha'], potencia = valores[j]['avg'])
	TempDB.objects.all().delete()
	item += 1


choices_temperaturas = [ "drxtempifcal", "drxtempdig", "drxtempana", "drx1tempifcal", "drx1tempdig", "drx1tempana", "ecupt100temp_1" ]
item = 0
while item < len(choices_temperaturas):
	for line in range(len(lines)):
		tag = lines[line].split('.')[0][21:]
		if tag == choices_temperaturas[item]:
			fechahora = datetime.strptime(lines[line][:16],"%Y-%m-%dT%H:%M")
			fechahora = fechahora.replace(minute = ((fechahora.minute/10)*10))
			fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
			valor = float(lines[line].split('>')[-1][:-2])
			TempDB.objects.create(tag = tag, fecha = fechahora, valor = valor)
	valores = TempDB.objects.filter(tag=choices_temperaturas[item]).values('fecha').annotate(avg=Avg('valor'))
	for j in range(len(valores)):
		Temperaturas.objects.create(sensor = choices_temperaturas[item], fecha = valores[j]['fecha'], temperatura = valores[j]['avg'])
	TempDB.objects.all().delete()
	item += 1


bite_path = './BITE/20160301.log'
bite_hoy = open(bite_path, 'r')
log_lines = bite_hoy.readlines()
bite_hoy.close()

i = 0
for j in (log_lines):
	if (j[9:36] == 'solenoid current value in A'):
		fechahora = datetime(2016,3,1,int(log_lines[i-152][29:31]),int(log_lines[i-152][32:34]))
		fechahora = fechahora.replace(minute = ((fechahora.minute/10)*10))
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		valor = float(j[42:-1])
		TempDB.objects.create(tag = "solenoid_cur", fecha = fechahora, valor = valor)
	i = (i + 1)

valores = TempDB.objects.values('fecha').annotate(avg=Avg('valor'))
for j in range(len(valores)):
	CorrienteSolenoide.objects.create(fecha = valores[j]['fecha'], corriente = valores[j]['avg'])
	
TempDB.objects.all().delete()

toc = time.time()

print "\nTiempo de parseo: " + str(toc-tic) + " segundos\n"

"""
TensionesReceptor.objects.all().delete()
PotenciasTransmisor.objects.all().delete()
Temperaturas.objects.all().delete()
CorrienteSolenoide.objects.all().delete()
TempDB.objects.all().delete()
"""