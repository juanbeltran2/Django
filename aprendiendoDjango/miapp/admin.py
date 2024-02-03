from django.contrib import admin
from .models import article, categoy   ### TRaemos los modelos que requerimos o todos (*)

# Register your models here.
admin.site.register(article)
admin.site.register(categoy)
