from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('articulos', views.articulo_completo),
	url(r'^$', views.articulos_detalle),
	# url('1', views.articulos_detalle),
]