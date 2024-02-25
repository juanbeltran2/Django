from blog.models import Category, Article

def get_categories( request ):

    # Traemos las categorias que se esten activas en los articulos en texto plano
    categories_in_use   =   Article.objects.filter( public=True ).values_list('category', flat=True)

    # Hacemos la consuta a la BD para traer lo que necesitamos de acuerdo a las categorias que esten en uso en los articulos
    categories = Category.objects.filter( id__in=categories_in_use).values_list( 'id', 'name' ) 

    return {
        'categories'    :   categories,
        'ids'           :   categories_in_use
        } 