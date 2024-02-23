"""
URL configuration for ProyectoDjango project.

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

### COnfiguracion inicial antes de mejorar las rutas
'''
# Cargamos las vistas de las apps que hemos creado
from mainapp import views  
from pages import views as page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),                ## Ruta por defecto
    path('inicio/', views.index, name="Inicio"),         ## Ruta del index
    path('sobre-nosotros/', views.about, name="about"),
    path('pagina/<str:slug>', page_views.page, name="page")
]
'''

# Nueva configuracion de rutas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('pages.urls')),
]