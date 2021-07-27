from django.contrib import admin
from .models import Product 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'active', 'featured')
    list_display_links = ('title', 'description')
    list_editable = ('price', 'active', 'featured')
    search_fields = ('title', )