from operator import mod
from pyexpat import model
from unicodedata import name
from django.db import models
from tabnanny import verbose


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True,default=0 ,verbose_name='Цена')
    
    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    

    