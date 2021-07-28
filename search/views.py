from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    template_name = "search/search.html"
    queryset = Product.objects.all()
    def get_queryset(self):
        request = self.request.GET['search']
        
        if request is not None:            
            return Product.objects.filter(title__icontains = request)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request.GET['search']
        context['pesquisa'] = request
        return context
        
        
    