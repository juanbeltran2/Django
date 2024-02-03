# Importamos los paquetes necesarios
from django.shortcuts import render, HttpResponse, redirect

# Importamos el modelo con las tablas de la BD
from miapp.models import *

# Libreria para operador logico OR
from django.db.models import Q

# Se llaman los metodos de creacion de formularios que se crearon en el script de forms.py
from miapp.forms import FormArticle

# Libreria para mensajes flash (sesion que se muestra 1 vez)
from django.contrib import messages

# Creo una la funcion, la cual sera llamada desde E:\Cursos\Django\aprendiendoDjango\aprendiendoDjango\urls.py
# Menu que se mostrara en todas las paginas
layout  =   """
    <h1> Sitio Web con Django </h1>
    <hr/>
    <ul>
        <li> Pagina de pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr/>
"""

def index( request ):
   
    nombre ='Jeremy'
    lenguajes   =   ['java','python','C++']
    year        =   2021
    hasta       =   range( year, 2051 )

    # Renderizamos o mostramos en el html (este debe estar configurado en las urls..... se envian datos a la vista por medio de un diccionario)
    return render(request, 'index.html', {
        'tittle'        :   'Inicio',
        'mi_variable'   :   'soy un dato de la vista',
        'nombre'        :   nombre,
        'lenguajes'     :   lenguajes,
        'years'         :   hasta
    })

def hola_mundo( request ):
    # print("request => ", request)
    return render(request,'hola_mundo.html')

def pagina( request, redirigir = 0 ):

    if redirigir == 1:
        # return redirect('/inicio/')                   # Redirigir a una pagina especifico
        # return redirect('/contacto/Juan/Beltran')     # Redirigir enviando parametros
        return redirect('Contacto', nombre="Paola", apellidos="Beltran")   # Redirigir por el nombre de una url

    return render(request, 'pagina.html',{
        'textoVacio'    :   '',
        'lista'         :   ['uno', 'dos', 'tres'],
        'textoPrueba'   :   'TextO de pRuEba'
    })

def contacto( request, nombre="", apellidos="" ):

    html = ""

    if nombre and apellidos:
        html += " <p> El nombre completo es: </p> "
        html += f"<h3> {nombre} {apellidos}  </h3>"
    return HttpResponse(layout + "<h2> Contacto </h2>" + html)

def crear_articulo( request,title, content, public  ):

    # Creamos una dupla con la informacion que se va a guardar
    articulo = article(
        title   =   title,
        content =   content,
        public  =   public
    )

    # Almacenamos el registro
    articulo.save()
    return HttpResponse(f"Articulo {articulo.title} creado:")

def consultar_articulo( request ):

    # Consultamos la BD para traer un solo articulo
    try:
        articulo    =   article.objects.get(title="Batman", public= True  )
        response    =   f"Articulo consultado: {articulo.title}"
    except:
        response    =   'Articulo no encontrado'

    return HttpResponse(response) 

def editar_articulo( request, id ):

    articulo = article.objects.get( pk=id )

    articulo.title      =   "Batman"
    articulo.content    =   "Pelicula"
    articulo.public     =   True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado por: {articulo.title}")

def consultar_articulos( request ):

    # Consultamos la BD para traer un todos los articulos
    #articulos   =   article.objects.all().order_by('-id')  # traer todos los articulos y Orderar de forma descendente
    articulos   =   article.objects.filter( public=True ).order_by('-id')  # traer todos los articulos y Orderar de forma descendente

    # articulos   =   article.objects.order_by('id')

    # Filtros
    # articulos   =   article.objects.filter(title__contains='Batman')

    # Operador OR (Se requiere importar la libreria Q )
    """
    articulos   =   article.objects.filter(
        Q(title__contains="2") | Q(title__contains="3") 
    )
    """

    # Excluir registros
    """
    articulos   =   article.objects.filter(
        title__contains='articulo'
        ).exclude(
            public=False
        )
    """
    # Consulta por SQL puro
    # articulos   =   article.objects.raw("SELECT * FROM miapp_article ")

    return render( request, 'articulos.html', {
        'articulos'   :   articulos
    }) 

def borrar_articulo( request, id ):

    articulo =  article.objects.get( pk=id )
    articulo.delete()

    return redirect('articulos')

def save_article( request  ):

    # Recibir y almaenar desde un formulario por metodo GET
    if request.method == 'GET':

        title   =   request.GET['title']
        content =   request.GET['content']
        public  =   request.GET['public']

        articulo = article(
            title   =   title,
            content =   content,
            public  =   public
        )

        # Almacenamos el registro
        articulo.save()

        return HttpResponse(f"Articulo {title} creado:")
    
    # Recibir y almaenar desde un formulario por metodo POST
    elif request.method == 'POST':

        title   =   request.POST['title']
        content =   request.POST['content']
        public  =   request.POST['public']

        articulo = article(
            title   =   title,
            content =   content,
            public  =   public
        )

        # Almacenamos el registro
        articulo.save()

        return HttpResponse(f"Articulo {title} creado:")

    else:
        return HttpResponse("<h2>No se ha podido guardar el artículo</h2>") 

def create_article(request):

    return render(request, 'create_article.html')

def create_full_article( request ):

    if request.method == 'POST':
        
        formulario = FormArticle( request.POST)

        if formulario.is_valid():
            data_form  =    formulario.cleaned_data  # Se obtienen los datos limpos del formulario

            title   =   data_form.get('title')
            content =   data_form['content']
            public  =   data_form['public']

            articulo = article(
                title   =   title,
                content =   content,
                public  =   public
            )

            # Almacenamos el registro
            articulo.save()

            # creo el mensaje flash
            messages.success( request, 'Articulo creado {0}'.format(articulo.id) )

            # return HttpResponse(title + ' ' + content + ' ' + str(public) )
            return redirect('articulos')
    else:

        # Funcion para crear los formularios que se encuentran en forms.py
        formulario = FormArticle()

    return render( request, 'create_full_article.html', {
        'form':formulario
    } )