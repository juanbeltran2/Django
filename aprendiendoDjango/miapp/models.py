from django.db import models

# Create your models here.

class article( models.Model ):
    title       =   models.CharField(max_length=150)
    content     =   models.TextField()
    image       =   models.ImageField( default='null')
    public      =   models.BooleanField()
    created_at  =   models.DateTimeField(auto_now_add=True)
    update_at   =   models.DateTimeField(auto_now=True)

class categoy( models.Model ):
    name            =   models.CharField(max_length=110)
    description     =   models.CharField(max_length=250)
    create_at       =   models.DateField()
