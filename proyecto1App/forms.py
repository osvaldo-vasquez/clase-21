from django import forms
from .models import libro

class libroFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre del libro')
    autor = forms.CharField(label='Autor')
    editorial = forms.CharField(label='Editorial')
    genero = forms.CharField(label='Género')
    sinopsis = forms.CharField(label='Sinópsis')
    numpag = forms.IntegerField(label='Número de páginas')
    fecha_pub = forms.DateField(label='Fecha de publicación (mm/dd/aaaa)')
    fecha_compra = forms.DateField(label='Fecha de compra (mm/dd/aaaa)')
    ISBN = forms.CharField(label='ISBN')
    formato = forms.ChoiceField(choices=libro.formato_op, required=True, widget=forms.RadioSelect, label='Formato')


