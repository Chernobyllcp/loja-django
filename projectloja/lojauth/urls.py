from django.urls import path
from lojauth import views

urlpatterns = [
    path('cadastrar/', views.cadastrar,name='cadastrar')
    
]
