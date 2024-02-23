from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

# Modificar el ttulo del panel de administracion de Django
title       =   'Proyecto con Django'
subtitle    =   'Panel de gestion'
admin.site.site_header  =   title
admin.site.site_title   =   title
admin.site.index_title  =   subtitle

