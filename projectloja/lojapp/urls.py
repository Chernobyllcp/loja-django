from django.urls import path
from lojapp import views

urlpatterns = [
    path('', views.index,name='index'),
    
]
