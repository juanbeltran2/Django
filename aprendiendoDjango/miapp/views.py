# Importamos los paquetes necesarios
from django.shortcuts import render, HttpResponse, redirect

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