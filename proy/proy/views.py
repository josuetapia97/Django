from django.http import HttpResponse
from django.template import Template, Context, loader
#from django.template import loader
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Mundo")


def saludo_html(request):
    doc = open("C:/Users/moenc/Documents/django/proy/proy/templates/temp.html")
    tmpl = Template(doc.read())
    doc.close()
    ctx = Context({"BY":"Josue"})
    text = tmpl.render(ctx)
    return HttpResponse(text)

def saludo_html_cargador(request):
    doc = loader.get_template('temp.html')
    dicc = {"BY":"Josue con cargador"}
    text = doc.render(dicc)
    return HttpResponse(text)

def saludo_render(request):

    return render(request,"temp.html",{"BY":"Josue render"})

def saludo_herencia(request):
    return render(request, "hija1.html",{"BY":"Josue herencia"})

def saludo_herencia2(request):
    return render(request, "hija2.html",{"BY":"Josue herencia"})
