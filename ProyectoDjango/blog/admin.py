from django.contrib import admin
from .models import Category, Article

# HAbilitamos las columnas a mostrar
class CategoryAdmin( admin.ModelAdmin ):
    readonly_fields =   ( 'created_at',)

class ArticleAdmin( admin.ModelAdmin ):
    readonly_fields =   ( 'created_at', 'update_at' )


# Register your models here.
admin.site.register(Category , CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
