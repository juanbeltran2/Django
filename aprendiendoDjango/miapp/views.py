# Importamos los paquetes necesarios
from django.shortcuts import render, HttpResponse, redirect

# Importamos el modelo con las tablas de la BD
from miapp.models import *

# Libreria para operador logico OR
from django.db.models import Q

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
        articulo    =   article.objects.get(title="segundo", public= True  )
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
    # articulos   =   article.objects.all()
    articulos   =   article.objects.order_by('id')

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