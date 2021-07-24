from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'lista de produtos'
        return context