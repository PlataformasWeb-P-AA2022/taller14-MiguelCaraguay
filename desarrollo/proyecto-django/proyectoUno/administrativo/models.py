from django.db import models

# Create your models here.

class Propietario(models.Model):
    opciones_nacionalidad = (
        ('ecuatoriana','Ecuatoriana'),
        ('peruana','Peruana'),
        ('colombiana','Colombiana'),
    )  
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField('edad')
    nacionalidad = models.CharField(max_length=30, choices=opciones_nacionalidad)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costo_departamento = models.IntegerField('costo departamento')
    num_cuartos = models.IntegerField('numero de cuartos')
    num_banios = models.CharField(max_length=100)
    valor_alicuota = models.FloatField(max_length=100)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%d %d %d %d" % (self.costo_departamento,
         self.num_cuartos,self.num_banios,self.valor_alicuota)