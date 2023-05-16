# models.py
from django.db import models

class Noticia(models.Model):
    class Meta:
        db_table = 'noticia'
    link = models.CharField(max_length=200)


    def __str__(self):
        return self.link

class Resultado(models.Model):
    class Meta:
        db_table = 'resultado-analise'
    noticias = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='resultados')
    resultado = models.BooleanField()
    fonte = models.CharField(max_length=45)
    titulo = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.noticias.link} {self.resultado}"