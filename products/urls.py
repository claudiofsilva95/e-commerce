from django.urls import path
from . import views 

app_name = 'products'

urlpatterns = [ 
    path('', views.ProductListView.as_view(), name='products'),
    path('destaque/', views.ProductFeaturedListView.as_view(), name='destaques'),
    path('category/<slug:slug>/', views.ProductListView.as_view(), name='listar_por_categoria'),

    path('<slug:slug>/', views.ProductDeatilView.as_view(), name='detail'),
]