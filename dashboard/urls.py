from django.conf.urls import include, url # Importa metodos Django
from . import views # Importa todas las Views (ninguna de momento)

urlpatterns = [
	url(r'^$', views.dashboard_home),
]