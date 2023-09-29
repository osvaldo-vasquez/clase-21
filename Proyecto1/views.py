from django.http import HttpResponse
from datetime import datetime
def saludo(request):
    return HttpResponse("Hola amigos")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos está en corto<br><br> ")

def fecha_Hora(request):
    dia = datetime.now()

    documentoDeTexto = f"Hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def mi_Nombre(request, nombre):

    name = f'mi nombre es:<br><br> {nombre}'

    return HttpResponse(name)
