from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lojapp.urls')),
    path('lojauth/', include('lojauth.urls')),

]
