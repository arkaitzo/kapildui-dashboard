from dashboard.models import *
from datetime import datetime
from django.utils import timezone


# python manage.py shell
bite_path = './BITE/radar1_BITE160301.log'
bite_hoy = open(bite_path, 'r')
lines = bite_hoy.readlines()
bite_hoy.close()


choices_fuentes_rx = [ "drxpowpos5", "drxpowpos33", "drxpowneg5", "drx1powpos5", "drx1powpos33", "drx1powneg5" ]
choices_canales_tx = [ "spbtxpowkw", "spbtxpowdpvkw" ]
choices_temperaturas = [ "drxtempifcal", "drxtempdig", "drxtempana", "drx1tempifcal", "drx1tempdig", "drx1tempana", "ecupt100temp_1" ]
for line in range(len(lines)):
	tag = lines[line].split('.')[0][21:]
	if tag in choices_fuentes_rx:
		fechahora = datetime.strptime(lines[line][:19],"%Y-%m-%dT%H:%M:%S")
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		tension = float(lines[line].split('>')[-1][:-2])
		TensionesReceptor.objects.create(fuente = tag, fecha = fechahora, tension = tension)
	elif tag in choices_canales_tx:
		fechahora = datetime.strptime(lines[line][:19],"%Y-%m-%dT%H:%M:%S")
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		potencia = float(lines[line].split('>')[-1][:-2])
		PotenciasTransmisor.objects.create(canal = tag, fecha = fechahora, potencia = potencia)
	elif tag in choices_temperaturas:
		fechahora = datetime.strptime(lines[line][:19],"%Y-%m-%dT%H:%M:%S")
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		temperatura = float(lines[line].split('>')[-1][:-2])
		Temperaturas.objects.create(sensor = tag, fecha = fechahora, temperatura = temperatura)

"""
# Tensiones cada 10 minutos (144 registros)
# Temperaturas cada 10 minutos (144 registros)
# Potencias cada 1 minuto (1440 registros)
"""

bite_path = './BITE/20160301.log'
bite_hoy = open(bite_path, 'r')
log_lines = bite_hoy.readlines()
bite_hoy.close()

i = 0
for line in log_lines:
	if line[9:36] == 'solenoid current value in A':
		fechahora = datetime(2016,03,01,int(log_lines[i-152][29:31]),int(log_lines[i-152][32:34]),int(log_lines[i-152][35:37]))
		fechahora = timezone.make_aware(fechahora, timezone.get_current_timezone())
		corriente = float(line[42:-1])
		CorrienteSolenoide.objects.create(fecha = fechahora, corriente = corriente)
	i += 1








