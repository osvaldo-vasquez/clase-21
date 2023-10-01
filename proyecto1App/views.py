from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "proyecto1App/index.html")

def cursos(request):
    return render(request, "proyecto1App/cursos.html")

def profesores(request):
    return render(request, "proyecto1App/profesores.html")

def estudiantes(request):
    return render(request, "proyecto1App/estudiantes.html")

def entregables(request):
    return render(request, "proyecto1App/entregables.html")