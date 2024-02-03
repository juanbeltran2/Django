########## Crear formularios basados en Clases

from django import forms
from django.core import validators    # libreria que nos ayuda a validar los tipos de datos

class FormArticle( forms.Form ):

    title   =   forms.CharField(
        label       =   "Titulo",
        max_length  =   20,
        required    =   True,
        widget      =   forms.TextInput(  # widget se utiliza para cambiar los atributos del html
            attrs={
                'placeholder'   :   'Ingresa el titulo',
                'class'         :   'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El titulo es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$', 'El titulo no cumple las condiciones', 'invalid_tittle')
        ]
    )

    content   =   forms.CharField(
        label       =   "Contenido",
        widget      =   forms.Textarea,  
        max_length  =   100,
        required    =   False
    )
    content.widget.attrs.update({       ########### esta es otra forma de modificar loa atributos
        'placeholder'   :   'Ingresa el contenido',
        'class'         :   'contenido_form_article',
        'id'            :   'contenido_form'
    })

    # Se crean las opciones que estaran en el select
    public_option = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label   =   'Publicado',  
        choices =   public_option
    )


