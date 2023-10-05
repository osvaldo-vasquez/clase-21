from django.urls import path
from proyecto1App import views

urlpatterns = [
    path('index/', views.inicio, name = "Inicio"),
    path('cursos/', views.cursos, name ="Cursos"),
    path('profesores/', views.profesores, name = "Profesores"),
    path('estudiantes/', views.estudiantes, name = "Estudiantes"),
    path('entregables/', views.entregables, name = "Entregables")
]