from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),                ## Ruta por defecto
    path('inicio/', views.index, name="Inicio"),         ## Ruta del index
]
