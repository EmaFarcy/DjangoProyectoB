from django.http import HttpResponse
import random

from django.shortcuts import render
from django.template import Context, Template, loader



def inicio(request):  #Para las views siempre utilizamos el request como primer parámetro. 
    return render(request, "indice/index.html", {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un título Grande</h1>
                        ''')

def numero_random(request):
    numero= random.randrange(15, 180)
    texto= f'<h1>Este es un número random: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto= f'<h1>Este es un número: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    #plantilla = open(r"/home/emanuel/Dropbox/Coderhouse/Curso Python/Django/MiSegundoProyecto/mi_proyecto/plantillas/mi_plantilla.html")
    #template= Template(plantilla.read())
     #context = Context(diccionario_de_datos)
    
    template= loader.get_template('mi_plantilla.html')
    
    nombre= 'Jorgelina'
    apellido= 'Atahualpa'
    lista=[3,5,1,7,2,9]
    
    diccionario_de_datos = {
        'nombre':  nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista
        
    }
    
    #plantilla_preparada = template.render(diccionario_de_datos)
    #return HttpResponse(plantilla_preparada)
    
    #version con render
    return render(request, 'mi_plantilla.html', diccionario_de_datos)


