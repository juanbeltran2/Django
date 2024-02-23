from pages.models import Page

def get_pages( request ):

    # Hacemos la consuta a la BD para traer lo que necesitamos
    pages = Page.objects.filter(visible=True).order_by('order').values_list( 'id', 'title', 'slug' ) # Traemos las columnas especificas en forma de tupla

    # pages = Page.objects.values_list( 'id', 'title', 'slug' ) # Traemos las columnas especificas en forma de lista

    return {
        'pages' : pages
    } 