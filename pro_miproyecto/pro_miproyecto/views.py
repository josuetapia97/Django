from django.http import HttpResponse
import datetime
#importamos template y contexto
from django.template import Template, Context
# loader
from django.template.loader import get_template

class Persona():

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista


    p1 = Persona("Pedrito","Jilipollas")
    #cargamos doc
    variable = "Juanito"
    element = ["juan","pedro","erasmo"]
    #doc_externo = open("C:/Users/moenc/Documents/django/pro_miproyecto/pro_miproyecto/plantilla.html")
    #modificamos settings en TEMPLATES
    doc_externo = get_template('plantilla.html')
    #cargamos template
    #plt = Template(doc_externo.read())
    #cerramos archivo
    #doc_externo.close()
    #creamos contexto

    #ctx = Context({"variable1": variable, "persona":p1,"element":element})
    #renderisamos
    #doc =  plt.render(ctx)
    ctx = {"variable1": variable, "persona":p1,"element":element}
    doc =  doc_externo.render(ctx)
    return HttpResponse(doc)

def despedida(request):
    return HttpResponse("Hola Mundo2!")

def horario(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
        <body>
            <div>
                Fecha y hora actuales {}
            </div>
        </body>
    </html>
    """.format(fecha_actual)
    return HttpResponse(documento)

def edad(request,edad,anio):
    #edadActual = 18
    periodo = anio - 2020
    edadFutura = edad + periodo
    return HttpResponse( """
    <html>
        <body>
            <div>
                En el año {} tendras {}
            </div>
        </body>
    </html>
    """.format(anio,edadFutura))
