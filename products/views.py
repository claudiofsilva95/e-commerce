from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.shortcuts import get_object_or_404


class ProductListView(ListView):
    category = None
    def get_queryset(self):
        queryset = Product.objects.all()
        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
        return queryset
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'lista de produtos'
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context

class ProductFeaturedListView(ListView):
    template_name = 'products/product_list.html'
    def get_queryset(self):        
        queryset = Product.objects.all().featured()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Produtos em destaque'
        return context


class ProductDeatilView(DetailView):
    queryset = Product.objects.all()

