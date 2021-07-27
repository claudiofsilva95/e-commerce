from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


        
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    
    def featured(self):
        return self.filter(featured=True, active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()


class Product(models.Model): #product_category
    title  = models.CharField(max_length=120, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00, verbose_name='Preço')
    slug = AutoSlugField(unique=True, always_update=False, populate_from='title')
    image = models.ImageField(upload_to = 'media/%d/%m/%Y/', blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False, verbose_name='Destaque')

    objects = ProductManager()
    
    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})
