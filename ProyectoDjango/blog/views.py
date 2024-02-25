from django.shortcuts import render, get_object_or_404  # Importamos la libreria del error 404 
from django.core.paginator import Paginator             # importamos la libreria de paginacion
from blog.models import Category, Article

# Create your views here.
def list(request ):

    # Obtengo todos los articulos
    articles    =   Article.objects.all()

    # Pagino los articulos y la cantidad de articulos por pagina
    paginator   =   Paginator( articles, 1 )

    # Recojo numero pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page) 

    # print(articles.query)

    return render( request, 'articles/list.html',{
        'title'     :   'Articulos',
        'articles'  :   page_articles
    } )

def category( request, category_id ):

    # category    =   Category.objects.get( id=category_id )  Realiza la consulta normal

    # Realiza la consulta al modelo pero si hay error, utiliza la libreria de 404
    category    =   get_object_or_404( Category,  id=category_id )    
    articles    =   Article.objects.filter( category = category )

    return render( request, 'categories\category.html',{
        'category'  :   category,
        'articles'  :   articles
    })

def article( request, article_id ):

    article =   get_object_or_404( Article, id=article_id  )

    return render( request, 'articles/detail.html',{
        'article'   :   article 
    })