from django.db import models


#DEPARTAMENTOS
class Departamento(models.Model):
    codigo = models.CharField(verbose_name='Codigo', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    class Meta:
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"