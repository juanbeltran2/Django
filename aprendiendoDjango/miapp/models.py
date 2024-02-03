from django.db import models


'''
############### Migracion ################################
python manage.py makemigrations         ===> Creamos la tarea de migracion
python manage.py sqlmigrate pages 0001  ===> Indicamos la migracion que vamos a realizar
python manage.py migrate                ===> Ejecutamos la migracion

'''

# Create your models here.

class article( models.Model ):
    title       =   models.CharField(max_length=150, verbose_name="Titulo")
    content     =   models.TextField()
    image       =   models.ImageField( default='null', upload_to="articles")
    public      =   models.BooleanField()
    created_at  =   models.DateTimeField(auto_now_add=True)
    update_at   =   models.DateTimeField(auto_now=True)

    # Adicionamos la clase Meta para modificar la visualizacion del panel de administracion de django
    class Meta:
        verbose_name        =   "Articulo"
        verbose_name_plural =   "Articulos"
        ordering            =   ['public']

    def __str__(self):

        if self.public:
            publico =   "(Publicado)"
        else:
            publico =   "(Privado)"

        return f"{self.title} {publico}"

class categoy( models.Model ):
    name            =   models.CharField(max_length=110)
    description     =   models.CharField(max_length=250)
    create_at       =   models.DateField()

    class Meta:
        verbose_name        =   "Categoria"
        verbose_name_plural =   "Categorias"
        ordering            =   ['id']
