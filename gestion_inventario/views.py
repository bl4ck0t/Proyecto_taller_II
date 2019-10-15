from django.shortcuts import render,redirect
from gestion_inventario.models import usuario,formulario,concepto
from gestion_inventario.forms import usuarioForm,formularioForm,conceptoForm

def buscar_formulario(request):
    formularios=formulario.objects.all()
    return render(request,"buscar_formulario.html",{'formularios':formularios})

