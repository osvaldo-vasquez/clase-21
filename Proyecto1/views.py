# Agregamos al encabezado del archivo el import de Template y de Context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def probando_template(request):

    nombre = "Osvaldo"
    apellido = "Vasquez"
    diccionario = {"nombre": nombre, "apellido": apellido}

    # Abrimos el archivo html
    mi_html = open('./Proyecto1/templates/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacio para que funcione
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizandolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
def usando_Loader(request):
    nombre = "Osvaldo"
    apellido = "Vasquez"
    diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4, 8, 9, 10, 7, 8]}
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
