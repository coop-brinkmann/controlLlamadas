"""controlLlamadas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from control.views import Home, importar_lama, importar_ama, llamadas_datatables_view, ListadoLlamada, \
    get_tipos_llamadas_distinct

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^lama/$', importar_lama, name='importar_lama'),
    url(r'^ama/$', importar_ama, name='importar_ama'),
    url(r'^llamadas/$', ListadoLlamada.as_view(), name='listado_llamadas'),
    url(r'^api/llamadas_dt/$', llamadas_datatables_view, name='llamadas_dt'),
    url(r'^api/get_tipos_llamadas_distinct/$', get_tipos_llamadas_distinct, name='get_tipos_llamadas_distinct'),

]
