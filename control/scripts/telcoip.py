import csv
from control.models import Prefijo
from controlLlamadas.settings import BASE_DIR

print "BASEDIR: %s" % BASE_DIR

with open("%s/nume.csv" % BASE_DIR) as f:
    reader = csv.reader(f)
    i = 1
    for row in reader:
        modalidad = "NARANJA"
        if row[-10] == "BASICA":
            modalidad = "BAS"
        elif row[-10] == "CPP":
            modalidad = "MOV"
        elif row[-10] == "ESP":
            modalidad = "ESP"
        elif row[-10] == "INTF" or row[-10] == "INTM":
            modalidad = "INT"
        elif row[-10] == "MPP":
            modalidad = "MPP"
        elif row[-10] == "NOGEO":
            modalidad = "NOG"
        localidad = row[-9]
        try:
            caracteristica = int(row[-8])
        except Exception:
            caracteristica = 0
        try:
            bloque = int(row[-7])
        except Exception:
            bloque = 0
        pre = Prefijo(modalidad=modalidad, localidad=localidad, caracteristica=caracteristica, bloque=bloque)
        pre.save()
        print i
        i += 1
    f.close()
