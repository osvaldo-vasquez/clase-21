from django.shortcuts import render
from django.http import HttpResponse
from proyecto1App.models import libro
from proyecto1App.models import revista
from proyecto1App.models import autor
from proyecto1App.forms import libroFormulario
from proyecto1App.forms import revistaFormulario
from proyecto1App.forms import autorFormulario

def inicio(request):
    return render(request, "proyecto1App/index.html")

def autores(request):
    return render(request, "proyecto1App/autores.html")

def ebooks(request):
    return render(request, "proyecto1App/ebooks.html")

def libroForm(request):
 
    if request.method == "POST":
 
        miFormulario = libroFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  nuevo_libro = libro(nombre=informacion["nombre"], autor=informacion["autor"], editorial=informacion["editorial"], genero=informacion["genero"], sinopsis=informacion["sinopsis"], numpag=informacion['num_pag'], fecha_pub=informacion['fecha_pub'], fecha_compra=informacion['fecha_compra'], ISBN =informacion['ISBN'], formato =informacion['formato'])
                  nuevo_libro.save()
                  return render(request, "proyecto1App/index.html")
    else:
            miFormulario = libroFormulario()
 
    return render(request, "proyecto1App/libroFormulario.html", {"miFormulario": miFormulario})

def revistaForm(request):
 
    if request.method == "POST":
 
        miFormulario = revistaFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  nueva_revista = revista(nombre=informacion["nombre"], titulo=informacion["titulo"], numero = informacion["numero"], web = informacion["web"], genero=informacion["genero"], temas=informacion["temas"], fecha_pub=informacion['fecha_pub'], fecha_compra=informacion['fecha_compra'], formato =informacion['formato'])
                  nueva_revista.save()
                  return render(request, "proyecto1App/index.html")
    else:
            miFormulario = revistaFormulario()
 
    return render(request, "proyecto1App/revistaFormulario.html", {"miFormulario": miFormulario})


def autorForm(request):
 
    if request.method == "POST":
 
        miFormulario = autorFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  nuevo_autor = autor(nombre=informacion["nombre"],apellido=informacion["apellido"], email = informacion["email"], nacionalidad = informacion["nacionalidad"], genero=informacion["genero"], premios=informacion["premios"], biografia=informacion['biografia'])
                  nuevo_autor.save()
                  return render(request, "proyecto1App/index.html")
    else:
            miFormulario = autorFormulario()
 
    return render(request, "proyecto1App/autorFormulario.html", {"miFormulario": miFormulario})

def buscarLibro(request):
    return render(request, "proyecto1App/buscarLibro.html")

def buscar(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         buscar_libro = libro.objects.filter(nombre__icontains = nombre) # Filtra el libro que se está buscando
         return render(request, "proyecto1App/resultadosBusqueda.html", {"nombre": nombre, "Libros":buscar_libro})

    else:
         respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def leerLibros(request):
    libros =  libro.objects.all() # Trae todos los libros
    return render(request, "proyecto1App/leerLibros.html", {"libros":libros})

def leerRevistas(request):
    revistas =  revista.objects.all() # Trae todos las revistas
    return render(request, "proyecto1App/leerRevistas.html", {"revistas":revistas})

def leerAutores(request):
    autores =  autor.objects.all() # Trae todos las revistas
    return render(request, "proyecto1App/leerAutores.html", {"autores":autores})