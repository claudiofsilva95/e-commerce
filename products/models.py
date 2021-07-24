from django.db import models

class Product(models.Model): #product_category
    title  = models.CharField(max_length=120, verbose_name='Preço')
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00, verbose_name='Preço')

    def __str__(self):
        return self.title