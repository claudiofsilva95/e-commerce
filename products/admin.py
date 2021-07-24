from django.contrib import admin
from .models import Product 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
    list_display_links = ('title', 'description')
    list_editable = ('price', )
    search_fields = ('title', )