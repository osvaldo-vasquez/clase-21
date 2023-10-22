from django.shortcuts import render, redirect
from django.http import HttpResponse
from proyecto1App.models import libro
from proyecto1App.models import revista
from proyecto1App.models import autor
from proyecto1App.forms import libroFormulario
from proyecto1App.forms import revistaFormulario
from proyecto1App.forms import autorFormulario

def inicio(request):
    return render(request, "proyecto1App/index.html")

def ebooks(request):
    return render(request, "proyecto1App/ebooks.html")

def libroForm(request):
 
    if request.method == "POST":
 
        miFormulario = libroFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  nuevo_libro = libro(nombre=informacion["nombre"], autor=informacion["autor"], editorial=informacion["editorial"], genero=informacion["genero"], sinopsis=informacion["sinopsis"], numpag=informacion['numpag'], fecha_pub=informacion['fecha_pub'], fecha_compra=informacion['fecha_compra'], ISBN =informacion['ISBN'], formato =informacion['formato'])
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

def borrar_libro(request, libro_id):
    
    libro_eliminar = libro.objects.get(id=int(libro_id))
    libro_eliminar.delete()
    return redirect('leerLibros')

def borrar_revista(request, revista_id):
    
    revista_eliminar = revista.objects.get(id=int(revista_id))
    revista_eliminar.delete()
    return redirect('leerRevistas')

def borrar_autor(request, autor_id):
    
    autor_eliminar = autor.objects.get(id=int(autor_id))
    autor_eliminar.delete()
    return redirect('leerAutores')

def editar_libro(request, libro_id):
    libroAeditar = libro.objects.get(id = libro_id)
    if request.method == "POST":
        
        
        miFormulario = libroFormulario(request.POST)

        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  libroAeditar.nombre = informacion["nombre"]
                  libroAeditar.autor = informacion["autor"]
                  libroAeditar.editorial = informacion["editorial"]
                  libroAeditar.genero = informacion["genero"]
                  libroAeditar.numpag = informacion["numpag"]
                  libroAeditar.fecha_pub = informacion["fecha_pub"]
                  libroAeditar.fecha_compra = informacion["fecha_compra"]
                  libroAeditar.ISBN = informacion["ISBN"]
                  libroAeditar.formato = informacion["formato"]
                  libroAeditar.save()
                  return redirect('leerLibros')
    else:
            miFormulario = libroFormulario(initial = {"nombre":libroAeditar.nombre, "autor":libroAeditar.autor, "editorial":libroAeditar.editorial,
                                            "genero":libroAeditar.genero, "sinopsis":libroAeditar.sinopsis, "numpag": libroAeditar.numpag, "fecha_pub":libroAeditar.fecha_pub,
                                            "fecha_compra":libroAeditar.fecha_compra, "ISBN":libroAeditar.ISBN, "formato":libroAeditar.formato})
 
    return render(request, "proyecto1App/libroFormulario.html", {"miFormulario": miFormulario})

def editar_revista(request, revista_id):
    revistaAeditar = revista.objects.get(id = revista_id)
    if request.method == "POST":
                
        miFormulario = revistaFormulario(request.POST)

        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  revistaAeditar.nombre = informacion["nombre"]
                  revistaAeditar.titulo = informacion["titulo"]
                  revistaAeditar.numero = informacion["numero"]
                  revistaAeditar.web = informacion["web"]
                  revistaAeditar.genero = informacion["genero"]
                  revistaAeditar.temas = informacion["temas"]
                  revistaAeditar.fecha_pub = informacion["fecha_pub"]
                  revistaAeditar.fecha_compra = informacion["fecha_compra"]
                  revistaAeditar.formato = informacion["formato"]
                  revistaAeditar.save()
                  return redirect('leerRevistas')
    else:
            miFormulario = revistaFormulario(initial = {"nombre":revistaAeditar.nombre, "titulo":revistaAeditar.titulo, "numero":revistaAeditar.numero,
                                            "web":revistaAeditar.web, "genero":revistaAeditar.genero, "temas": revistaAeditar.temas, "fecha_pub":revistaAeditar.fecha_pub,
                                            "fecha_compra":revistaAeditar.fecha_compra, "formato":revistaAeditar})
 
    return render(request, "proyecto1App/libroFormulario.html", {"miFormulario": miFormulario})

def editar_autor(request, autor_id):

    autorAeditar = autor.objects.get(id = autor_id)
 
    if request.method == "POST":
 
        miFormulario = autorFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  autorAeditar.nombre = informacion["nombre"]
                  autorAeditar.apellido = informacion["apellido"]
                  autorAeditar.email = informacion["email"]
                  autorAeditar.nacionalidad = informacion["nacionalidad"]
                  autorAeditar.genero = informacion["genero"]
                  autorAeditar.premios = informacion["premios"]
                  autorAeditar.biografia = informacion["biografia"]
                  autorAeditar.save()
                  return redirect('leerAutores')
    else:
            miFormulario = autorFormulario(initial = {"nombre":autorAeditar.nombre, "apellido":autorAeditar.apellido, "email":autorAeditar.email, "nacionalidad":autorAeditar.nacionalidad,
                                                       "genero":autorAeditar.genero, "premios":autorAeditar.premios, "biografia":autorAeditar.biografia})
 
    return render(request, "proyecto1App/autorFormulario.html", {"miFormulario": miFormulario})

      