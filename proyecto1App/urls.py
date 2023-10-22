from django.urls import path
from proyecto1App import views

urlpatterns = [
    path('index/', views.inicio, name = "Inicio"),
    path('autores/', views.autores, name = "Autores"),
    path('ebooks/', views.ebooks, name = "eBooks"),
    path('revistas/', views.revistas, name = "Revistas"),
    path('libroForm/', views.libroForm, name = "libroForm"),
    path('revistaForm/', views.revistaForm, name = "revistaForm"),
    path('buscarLibro/', views.buscarLibro, name = "buscarLibro"),
    path('buscar/', views.buscar),
    path('leerLibros/', views.leerLibros, name = "leerLibros"),
]