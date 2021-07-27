from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404


class ProductListView(ListView):

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'lista de produtos'
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

