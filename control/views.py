import json
import re
from datetime import datetime, timedelta
from StringIO import StringIO

import math
from django.core import serializers
from django.db.models.aggregates import Count, Sum
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic.base import TemplateView
from control.forms import LamaForm, AmaForm
from control.models import Llamada, Prefijo


class Home(TemplateView):
    template_name = "home.html"


def importar_lama(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LamaForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            lama = request.FILES['lama']
            registros_saltados = 0
            registros_duplicados = 0
            registros_insertados = 0
            duplicados = []
            registros_totales = len(lama.readlines()) - 3
            for linea in lama:
                continua = True if linea[64] == '*' else False
                if registros_saltados <= 2 or continua:
                    registros_saltados += 1
                    continue
                '''
                asterisco_cont_llamada = linea[64]
                numero_a = linea[0:13]
                numero_b = linea[13:30]
                fecha_hora = linea[30:44]
                duracion = linea[44:51]
                clave = linea[51:54]
                corredor = linea[68:76]
                '''
                numero_a = linea[0:13].strip()
                fecha_hora = datetime.strptime(linea[30:44], "%y-%m-%d %H:%M")
                numero_b = linea[13:30].strip()
                tipo_llamada = "SA"
                celular = False
                if numero_b.startswith('400') or numero_b.startswith('455') or numero_b.startswith(
                        '401') or len(numero_b) == 6:  # LLAMADA LOCAL
                    numero_b = '3562' + numero_b
                if numero_b[0] == "0" and numero_b[1] != "8":
                    numero_b = numero_b[1:]
                if numero_b.startswith("15"):
                    numero_b = '3562' + numero_b[2:]
                    celular = True

                match1 = re.match(r'^\d{2}15', numero_b)
                match2 = re.match(r'^\d{3}15', numero_b)
                match3 = re.match(r'^\d{4}15', numero_b)
                if match3:
                    caracteristica = numero_b[0:4]
                    movqs = Prefijo.objects.filter(modalidad="MOV", caracteristica=caracteristica)
                    if movqs:
                        a = 0
                        resultado = ""
                        while a < len(numero_b):
                            resultado += numero_b[a]
                            if a == 3:
                                a = 6
                            else:
                                a += 1
                        numero_b = resultado
                        celular = True

                elif match2:
                    caracteristica = numero_b[0:3]
                    movqs = Prefijo.objects.filter(modalidad="MOV", caracteristica=caracteristica)
                    if movqs:
                        a = 0
                        resultado = ""
                        while a < len(numero_b):
                            resultado += numero_b[a]
                            if a == 2:
                                a = 5
                            else:
                                a += 1
                        numero_b = resultado
                        celular = True
                elif match1:
                    caracteristica = numero_b[0:2]
                    movqs = Prefijo.objects.filter(modalidad="MOV", caracteristica=caracteristica)
                    if movqs:
                        a = 0
                        resultado = ""
                        while a < len(numero_b):
                            resultado += numero_b[a]
                            if a == 1:
                                a = 4
                            else:
                                a += 1
                        numero_b = resultado
                        celular = True

                duracion = int(math.ceil(float(linea[44:51].strip()) / 60))
                clave = int(linea[51:54].strip())
                corredor = "NA"
                if linea[68:75].startswith("1-5-1"):
                    corredor = "CO"
                elif linea[68:75].startswith("1-2-0") or linea[68:75].startswith("1-3-0"):
                    corredor = "TE"
                ll, creado = Llamada.objects.get_or_create(fecha_hora=fecha_hora, numero_a=numero_a, numero_b=numero_b,
                                                           celular=celular, tipo=tipo_llamada, duracion=duracion,
                                                           clave=clave, corredor=corredor)
                if creado:
                    registros_insertados += 1
                else:
                    boolean_celular = "Si" if celular == True else "No"
                    duplicados.append(
                        "F/H:%s -- A:%s -- B:%s -- Celular:%s -- Tipo:%s -- Duracion:%smin -- Corredor:%s" % (
                            fecha_hora, numero_a, numero_b, boolean_celular, tipo_llamada, duracion, corredor))
                    registros_duplicados += 1
            registros_saltados -= 3
            coincide_suma = True if (
                                    registros_duplicados + registros_saltados + registros_insertados) == registros_totales else False
            # ...
            # redirect to a new URL:
            return render_to_response("lama_success.html", {"registros_saltados": registros_saltados,
                                                            "registros_duplicados": registros_duplicados,
                                                            "registros_insertados": registros_insertados,
                                                            "registros_totales": registros_totales,
                                                            "coincide_suma": coincide_suma,
                                                            "detalle_duplicados": duplicados})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = LamaForm()

    return render(request, 'lama.html', {'form': form})


def importar_ama(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AmaForm(request.POST, request.FILES)
        # check whether it's valid:
        form.is_valid()
        print form.errors
        if form.is_valid():
            # process the data in form.cleaned_data as required
            ama = request.FILES['ama']
            registros_saltados = 0
            registros_duplicados = 0
            registros_insertados = 0
            duplicados = []
            registros_totales = len(ama.readlines()) - 3
            for linea in ama:
                if linea[64] == '*' or linea[9:19].startswith("3562401") or linea[9:19] == '3562455997':
                    continua = True
                else:
                    continua = False
                if registros_saltados <= 2 or continua:
                    registros_saltados += 1
                    continue
                '''
                asterisco_cont_llamada = linea[80]
                numero_a = linea[9:19]
                numero_b = linea[25:39]
                fecha_hora = linea[49:65]
                duracion = linea[68:72]
                corredor = linea[0:6]
                '''
                numero_a = linea[9:19].strip()
                fecha_hora = datetime.strptime(linea[49:65], "%Y-%m-%d %H:%M")
                numero_b = linea[25:39].strip()
                if len(numero_b) == 6:
                    numero_b = "3562" + numero_b
                else:
                    numero_b = numero_b[-10:]
                tipo_llamada = "EN"
                celular = False
                movqs = Prefijo.objects.filter(modalidad="MOV")
                a = 7
                while a >= 2:
                    try:
                        qs = movqs.get(completo=numero_a[:a])
                    except Prefijo.DoesNotExist:
                        a -= 1
                        continue
                    if qs:
                        celular = True
                        break
                duracion = int(math.ceil(float(linea[68:72].strip()) / 60))
                corredor = "NA"
                if linea[0:6] == "COSEL7":
                    corredor = "CO"
                elif linea[0:6] == "SANFCO" or linea[0:6] == "LOCSFO":
                    corredor = "TE"
                ll, creado = Llamada.objects.get_or_create(fecha_hora=fecha_hora, numero_a=numero_a, numero_b=numero_b,
                                                           celular=celular, tipo=tipo_llamada, duracion=duracion,
                                                           corredor=corredor)
                if creado:
                    registros_insertados += 1
                else:
                    boolean_celular = "Si" if celular == True else "No"
                    duplicados.append(
                        "F/H:%s -- A:%s -- B:%s -- Celular:%s -- Tipo:%s -- Duracion:%s -- Corredor:%s" % (
                            fecha_hora, numero_a, numero_b, boolean_celular, tipo_llamada, duracion, corredor))
                    registros_duplicados += 1
            registros_saltados -= 3
            coincide_suma = True if (
                                    registros_duplicados + registros_saltados + registros_insertados) == registros_totales else False
            # ...
            # redirect to a new URL:
            return render_to_response("ama_success.html", {"registros_saltados": registros_saltados,
                                                           "registros_duplicados": registros_duplicados,
                                                           "registros_insertados": registros_insertados,
                                                           "registros_totales": registros_totales,
                                                           "coincide_suma": coincide_suma,
                                                           "detalle_duplicados": duplicados})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = AmaForm()

    return render(request, 'ama.html', {'form': form})


class ListadoLlamada(TemplateView):
    template_name = "listado.html"


def llamadas_datatables_view(request):
    individual_searchs_i = {}
    for item in request.GET:
        match = re.match(r'columns\[(\d+)\]\[search\]\[value\]', item)
        if match and request.GET[item]:
            individual_searchs_i[int(match.group(1))] = request.GET[item]
    objects = Llamada.objects.all()
    list_display = ['get_fecha_hora', 'tipo', 'numero_a', 'numero_b', 'celular', 'duracion', 'clave', 'corredor']
    list_real_names = ['fecha_hora', 'tipo', 'numero_a', 'numero_b', 'celular', 'duracion', 'clave', 'corredor']
    list_global_search = ['numero_a', 'numero_b']
    dict_pos_names = {0: 'fecha_hora', 1: 'tipo', 2: 'numero_a', 3: 'numero_b', 4: 'celular', 5: 'duracion', 6: 'clave',
                      7: 'corredor'}
    print "INDIV SEARCH: %s" % individual_searchs_i
    # Cuenta total de articulos:
    recordsTotal = objects.count()

    # Filtrado de los articulos
    search = request.GET['search[value]']
    queriesg = []
    for item in list_global_search:
        queriesg.append(Q(**{item + '__icontains': search}))
    qsg = reduce(lambda x, y: x | y, queriesg)
    print qsg
    queriesi = []
    for k, v in individual_searchs_i.iteritems():
        if v == 'false':
            queriesi.append(Q(**{dict_pos_names[k]: False}))
        elif v == 'true':
            queriesi.append(Q(**{dict_pos_names[k]: True}))
        elif k == 0:
            desde = datetime.strptime(v.split("&&")[0], "%d-%m-%Y")
            hasta = datetime.strptime(v.split("&&")[1], "%d-%m-%Y") + timedelta(hours=23, minutes=59, seconds=59)
            queriesi.append(Q(**{dict_pos_names[k] + '__range': (desde, hasta)}))
        else:
            queriesi.append(Q(**{dict_pos_names[k] + '__icontains': v}))
    qsi = reduce(lambda x, y: x & y, queriesi) if queriesi else None
    print qsi
    objects = objects.filter(qsg & qsi) if qsi else objects.filter(qsg)

    # Ordenado
    order = dict(enumerate(list_real_names))
    dirs = {'asc': '', 'desc': '-'}
    ordering = dirs[request.GET['order[0][dir]']] + order[int(request.GET['order[0][column]'])]
    objects = objects.order_by(ordering)

    # Conteo de articulos despues dle filtrado
    recordsFiltered = objects.count()
    agg = objects.aggregate(Count('numero_a'), Sum('duracion'))

    # finally, slice according to length sent by dataTables:
    start = int(request.GET['start'])
    length = int(request.GET['length'])
    objects = objects[start: (start + length)]

    # extract information
    # data = [map(lambda field: _getattr_foreingkey(obj, field), list_display) for obj in objects]
    data = []
    for obj in objects:
        row = map(lambda field: getattr(obj, field), list_display)
        data.append(row)

    # define response
    response = {
        'data': data,
        'recordsTotal': recordsTotal,
        'recordsFiltered': recordsFiltered,
        'draw': request.GET['draw'],
        'total_llamadas': agg['numero_a__count'],
        'total_minutos': agg['duracion__sum']
    }

    # serialize to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return HttpResponse(s.read())


def get_tipos_llamadas_distinct(request):
    tipos = []
    map(lambda x: tipos.append(x['tipo']), Llamada.objects.all().values('tipo').distinct())
    s = StringIO()
    json.dump(tipos, s)
    s.seek(0)
    return HttpResponse(s.read())
