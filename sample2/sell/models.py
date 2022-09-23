from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True,default=0 ,verbose_name='Цена')
    
    def __str__(self):
        return self.name
    

    