"""
URL configuration for NutriStyle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name="Home"),
    #path('servicios/', include('servicios.urls')),

    #path('blog/', include('blog.urls')), #nosotros

    path('contacto/', include('contacto.urls')),

    path('autenticacion/', include('autenticacion.urls')),

    path('tienda/', include('tienda.urls')),  

    path('carro/', include('carro.urls')),  

    path('pedidos/', include('pedidos.urls')),  

    path('', include('crud.urls')),
    #path('procesar_pedido/', views.procesar_pedido, name='procesar_pedido'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
