# Se crean filtros de template personalizados

from django import template

# se crea la variable de templates
register = template.Library()

# Se crea un decorador
@register.filter(name='saludo')
def saludo(value):
    return f"<h1 style='color:red;'>Bienvenido, {value}  </h1> "