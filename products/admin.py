from django.contrib import admin
from .models import Category, Product 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'active', 'featured')
    list_display_links = ('title', 'category')
    list_editable = ('price', 'active', 'featured')
    search_fields = ('title', )
    list_filter = ('category', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass