from django.urls import path
from lojauth import views

urlpatterns = [
    path('cadastrar/', views.cadastrar,name='cadastrar'),
    path('login/', views.handlelogin,name='handlelogin'),
    path('logout/', views.handlelogout,name='handlelogout'),
    
]
