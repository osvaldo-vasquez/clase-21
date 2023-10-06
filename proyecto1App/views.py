from django.shortcuts import render
from django.http import HttpResponse
from proyecto1App.models import libro
from proyecto1App.forms import libroFormulario

def inicio(request):
    return render(request, "proyecto1App/index.html")

def libros(request):
    return render(request, "proyecto1App/libros.html")

def autores(request):
    return render(request, "proyecto1App/autores.html")

def ebooks(request):
    return render(request, "proyecto1App/ebooks.html")

def revistas(request):
    return render(request, "proyecto1App/revistas.html")
 
def libroForm(request):
 
    if request.method == "POST":
 
        miFormulario = libroFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  libro = libro(nombre=informacion["nombre"], autor=informacion["autor"], editorial=informacion["editorial"], genero=informacion["genero"], sinopsis=informacion["sinopsis"], numpag=informacion["numpag"])
                  libro.save()
                  return render(request, "proyecto1App/index.html")
    else:
            miFormulario = libroFormulario()
 
    return render(request, "proyecto1App/libroFormulario.html", {"miFormulario": miFormulario})
