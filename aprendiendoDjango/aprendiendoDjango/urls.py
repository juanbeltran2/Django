"""
URL configuration for aprendiendoDjango project.

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
from django.urls import path

# Importar app con mis vistas 
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Index"),                        # Ruta por defecto
    path('inicio/', views.index, name="Inicio"),                # Podemos reutilizar la misma url  
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),   # Importo la funcion desde la vista y es la ruta que se vera desde el navegador
    path('pagina-pruebas/', views.pagina, name="paginas"),   
    path('pagina-pruebas/<int:redirigir>', views.pagina, name="paginas"),  # redirigir a otra pagina
    path('contacto/', views.contacto, name="Contacto"),         # Envio de parametros por url
    path('contacto/<str:nombre>/', views.contacto, name="Contacto"), 
    path('contacto/<str:nombre>/<str:apellidos>', views.contacto, name="Contacto"), 
]
