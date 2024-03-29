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
from django.conf import settings

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
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('articulo/', views.consultar_articulo, name="articulo" ),
    path('editar-articulo/<int:id>', views.editar_articulo, name="editar_articulo"),
    path('articulos/', views.consultar_articulos, name="articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),
    path('save_article/', views.save_article, name="save"),
    path('create_article/', views.create_article, name="create"),
    path('create_full_article/', views.create_full_article, name="create_full"),
]

# Configuracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
