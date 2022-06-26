from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader


def index(request):
    return HttpResponse("Hola mundo.")
#cada def es una vista
#el numero en azul es lo que toca poner en el buscador
def fecha(request):
    fecha_actual = datetime.datetime.now() 
    documento= """<html>
    <body>
    <h2>
    fecha actual %s 
    <html/>
    <body/>
    <h2/>""" % fecha_actual
#no se usa el html asi sino que aparte con las plantillas.
    
    return HttpResponse(documento)
#el signo de porcentaje es para hacer que continue lo que esta al lado
#del otro signo de porcentaje.
#fecha te muestra la fecha y hora actual.
def Edad(request,Edad_actual,ago):
    #Edad_actual = 18, si le paso la edad por url no se necesita esta linea.
    periodo = ago - 2022
    Edad_futura = Edad_actual + periodo
    documento2="""<html>
    <body>
    <h2>
    En el año %s tendras %s años 
    <html/>
    <body/>
    <h2/>"""%(ago, Edad_futura)
 #esta para pasor por parametro por url la edad (ago).
 #este programa tu le entras un año y te dice que edad tendras en ese año.
    
    return HttpResponse(documento2)

def plantilla(request):
    nombre="Juan"
    Ahora=datetime.datetime.now()
    #doc_externo=open("C:/webs/Prueba2/cripto/web/plantillas/plantilla1.html")
    #hay una mejor de cargar el archivo con un loader   
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template("plantilla1.html")
    #ahora solo toca llamar al nombre de la plantilla.
    #ctx=Context({"nombre_persona":nombre,"Fecha_actual":Ahora})
    #tambien se puede poner listas en el context.
    #en el html para llamar a una variable o casa se usa es el nombre en verde.
    #documento3=doc_externo.render({"nombre_persona":nombre,"Fecha_actual":Ahora})
    #ahora el template se puede pasar directamente al render.
    
    return render(request, "plantilla1.html", {"nombre_persona":nombre,"Fecha_actual":Ahora})
#se pueden usar buqules for desde las plantillas 