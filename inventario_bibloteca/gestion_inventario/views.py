from django.shortcuts import render,redirect
from gestion_inventario.models import usuario,formulario,concepto
from gestion_inventario.forms import usuarioForm,formularioForm,conceptoForm

#def buscar_formulario(request):
    #formularios=formulario.objects.all()
    #return render(request,"buscar_formulario.html",{'formularios':formularios})

def buscar_formulario(request):
    if request.method == "POST":
        texto_busqueda = request.POST['texto_busqueda']
    else:
        texto_busqueda = ''
    formularios = formulario.objects.filter(nombre_responsable__contains=texto_busqueda)
    return render(request,"buscar_formulario.html",{'formularios':formularios})

def mostrar_formulario(request,id_formulario):
    formulario_mostrado=formulario.objects.get(id=id_formulario)
    conceptos=concepto.objects.all()
    #conceptos=concepto.objects.filter(id__exact=id_formulario)
    total_inventariados_ssue=0
    total_inventariados_libros=0
    total_inventariados_cd=0
    total_inventariados_resp=0
    for c in conceptos:
        total_inventariados_ssue+=c.ssue
        total_inventariados_libros+=c.libros
        total_inventariados_cd+=c.cd
        total_inventariados_resp+=c.resp 
    return render(request,"formulario.html",{
        'formulario':formulario_mostrado,
        'conceptos':conceptos,
        'total_inventariados_ssue':total_inventariados_ssue,
        'total_inventariados_libros':total_inventariados_libros,
        'total_inventariados_cd':total_inventariados_cd,
        'total_inventariados_resp':total_inventariados_resp})