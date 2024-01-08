########## Crear formularios basados en Clases

from django import forms

class FormArticle( forms.Form ):

    title   =   forms.CharField(
        label   =   "Titulo"
    )

    content   =   forms.CharField(
        label   =   "Contenido",
        widget  =   forms.Textarea
    )

    # Se crean las opciones que estaran en el select
    public_option = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label   =   'Publicado',  
        choices =   public_option
    )


