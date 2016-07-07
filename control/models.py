from django.db import models
from django.utils.datetime_safe import strftime


class DatosImportantes(models.Model):
    ultima_importacion_lama = models.DateTimeField(blank=True)
    ultima_importacion_telco = models.DateTimeField(blank=True)
    ultima_importacion_ama = models.DateTimeField(blank=True)


class Prefijo(models.Model):
    MODALIDAD = (("BAS", "Basica"),
                 ("MOV", "Movil"),
                 ("ESP", "Especial"),
                 ("INT", "Internacional"),
                 ("MPP", "MPP"),
                 ("NOG", "No Geografico"))

    caracteristica = models.IntegerField()
    bloque = models.IntegerField()
    localidad = models.CharField(max_length=300, default="")
    modalidad = models.CharField(max_length=3, choices=MODALIDAD, default="BAS")
    completo = models.BigIntegerField(default=0)


class Llamada(models.Model):
    TIPO_LLAMADA = (("EN", "Entrante"),
                    ("SA", "Saliente"))
    CORREDORES = (("TE", "Telecom"),
                  ("CO", "Colsecor"),
                  ("NA", "No Aplica"))

    fecha_hora = models.DateTimeField()
    tipo = models.CharField(max_length=2, choices=TIPO_LLAMADA)
    celular = models.BooleanField()  # Si es celular
    numero_a = models.CharField(max_length=30, default="")
    numero_b = models.CharField(max_length=30, default="")
    duracion = models.IntegerField()
    clave = models.IntegerField(default=0)
    corredor = models.CharField(max_length=2, choices=CORREDORES, default="NA")

    @property
    def get_fecha_hora(self):
        return strftime(self.fecha_hora, "%d-%m-%Y %H:%M")
