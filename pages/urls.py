from django.urls import path 
from . import views

app_name = 'pages'


urlpatterns = [ 
    path('', views.homePage, name='index'),
    path('sobre/', views.about_page, name='sobre'),
    path('contato/', views.contact_page, name='contato'),
]