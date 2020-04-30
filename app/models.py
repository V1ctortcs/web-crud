from django.db import models


class Produto(models.Model):
    cod = models.CharField(max_length=50, blank=False, unique=True)
    nome = models.CharField(max_length=50, blank=False)
    preco = models.CharField(max_length=50,blank=True)
    qtd = models.IntegerField(blank=True)

    def __str__(self):
        return self.cod
