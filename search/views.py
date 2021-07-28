from django.views.generic import ListView
from products.models import Product, Category

class SearchProductView(ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()
    category = None
    def get_queryset(self):
        request = self.request.GET['search']
        
        if request is not None:            
            return Product.objects.filter(title__icontains = request)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'lista de produtos'
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context
        
        
    