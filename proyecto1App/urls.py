from django.urls import path
from proyecto1App import views

urlpatterns = [
    path('index/', views.inicio, name = "Inicio"),
    path('ebooks/', views.ebooks, name = "eBooks"),
    path('autorForm/', views.autorForm, name = "autorForm"),
    path('libroForm/', views.libroForm, name = "libroForm"),
    path('revistaForm/', views.revistaForm, name = "revistaForm"),
    path('leerLibros/', views.leerLibros, name = "leerLibros"),
    path('leerRevistas/', views.leerRevistas, name = "leerRevistas"),
    path('leerAutores/', views.leerAutores, name = "leerAutores"),
    path('buscarLibro/', views.buscarLibro, name = "buscarLibro"),
    path('buscar/', views.buscar),
]