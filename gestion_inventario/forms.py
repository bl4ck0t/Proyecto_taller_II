from django import forms
from gestion_inventario.models import usuario,formulario,concepto

class usuarioForm(forms.ModelForm):
    class meta:
        model = usuario
        fields = "__all__"

class formularioForm(forms.ModelForm):
    class meta:
        model = formulario
        fields = "__all__"

class conceptoForm(forms.ModelForm):
    class meta:
        model = concepto
        fields = "__all__"