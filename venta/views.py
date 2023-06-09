from django.shortcuts import render
from django.http import JsonResponse

from .models import Usuario,Genero

import requests
import random


# Create your views here.
def inicio(request):
    context = {}
    return render(request,'venta/index.html',context)

def sign(request):    
    return render(request, 'venta/formulario-sign-up.html')

def login(request):    
    return render(request, 'venta/formulario-login.html')



def tienda(request):
    # Obtén el token de la API de Trefle
    trefle_api_token = "Sr5y3wPL13rMLu5U4TGYAT-AK8R1ILIHckPS3NbQ2Fs"
    
    # URL de la solicitud
    url = "https://trefle.io/api/v1/species/search"
    
    # Parámetros de la solicitud
    rosa = {
        "q": "Rosa chinensis",
        "limit": 1
    }

    spreading = {
        "q": "Spreading hedgeparsley",
        "limit": 1
    }    
    
    Christmastree = {
        "q": "Christmastree",
        "limit": 1
    }

    cannabis = {
        "q": "cannabis-sativa",
        "limit": 1
    }

    clover = {
        "q": "Cowgrass clover",
        "limit": 1
    }

    Indian = {
        "q": "Indian-dope",
        "limit": 1
    }    

    # Encabezados de la solicitud
    headers = {
        "Authorization": f"Bearer {trefle_api_token}"
    }
    
    # Realiza la solicitud GET a la API de Trefle
    response_rosa = requests.get(url, params=rosa, headers=headers)
    response_spreading = requests.get(url, params=spreading, headers=headers)
    response_Christmastree = requests.get(url, params=Christmastree, headers=headers)
    response_cannabis = requests.get(url, params=cannabis, headers=headers)    
    response_clover = requests.get(url, params=clover, headers=headers) 
    response_Indian = requests.get(url, params=Indian, headers=headers) 

    # Obtén los datos de la respuesta en formato JSON
    data_rosa = response_rosa.json()
    data_spreading = response_spreading.json()
    data_Christmastree = response_Christmastree.json()
    data_cannabis = response_cannabis.json()
    data_clover = response_clover.json()
    data_Indian = response_Indian.json()

    especies_rosa = data_rosa.get("data", [])
    especies_spreading = data_spreading.get("data", [])
    especies_Christmastree = data_Christmastree.get("data", [])
    especies_cannabis = data_cannabis.get("data", [])
    especies_clover = data_clover.get("data", [])
    especies_Indian = data_Indian.get("data", [])

    especies_totales = especies_rosa + especies_spreading + especies_Christmastree + especies_cannabis + especies_clover + especies_Indian

    for especie in especies_totales:
        especie["precio"] = generate_random_price()

    return render(request, "venta/tienda.html", {"especies_totales": especies_totales})

def generate_random_price():
    return random.randint(10000, 50000)



#CRUD#

def usuarios(request):
    return render(request,'venta/usuarios.html')

def usuariosList(request):
    #defino un objeto para trar el listado completo de usuarios desde la BD
    #Usuario.objects.all() <=> 'Select * From Usuario'
    usuarios= Usuario.objects.all()
    #cargo el objeto obtenido al contexto 
    contexto={
        'usuarios': usuarios
    }
    #agrego el contexto al retorno para que se vea en el template
    return render(request, 'venta/usuariosList.html', contexto)

def usuariosAdd(request):
    #si no es POST, se muestra formulario para agregar nuevos usuarios
    if request.method != "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request,'venta/usuariosAdd.html', context)
    else:
        #es un POST, por lo tanto se recuperan los datos del formulario
        #y se graban
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        apellido_paterno=request.POST["apellido_paterno"]
        apellido_materno=request.POST["apellido_materno"]
        fecha_nacimiento=request.POST["fecha_nacimiento"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]

        
        objGenero=Genero.objects.get(id_genero=genero)
        obj=Usuario.objects.create( rut=rut,
                                  nombre=nombre,
                                  apellido_paterno=apellido_paterno,
                                  apellido_materno=apellido_materno,
                                  fecha_nacimiento=fecha_nacimiento,
                                  id_genero=objGenero,
                                  telefono=telefono,
                                  email=email,
                                  direccion=direccion,

                                  activo=1)
        obj.save()
        context={'mensaje':"OK, datos grabados..."}
        return render(request, 'venta/usuariosAdd.html', context)

def usuariosDel(request, pk):
    context = {}
    try:
        usuario=Usuario.objects.get(rut=pk)
        usuario.delete()
        mensaje = "Los datos fueron eliminados con éxito!!!"
        usuarios= Usuario.objects.all()
        context ={'usuarios': usuarios, 'mensaje': mensaje}
        return render(request, 'venta/usuariosList.html', context)
    except:
        mensaje = "Error, rut no existe!!!"
        usuarios= Usuario.objects.all()
        context ={'usuarios': usuarios, 'mensaje': mensaje}
        return render(request, 'venta/usuariosList.html', context)

def usuariosEdit(request,pk):
    if pk != "":
        usuario=Usuario.objects.get(rut=pk)
        generos=Genero.objects.all()
        print(type(usuario.id_genero.genero))

        context = {'usuario': usuario, 'generos':generos}
        if usuario:
            return render (request,'venta/usuariosEdit.html',context)
        else:
            context={'mensaje': "Error, rut no existe..."}
            return render(request, 'venta/usuariosEdit.html', context)

def usuariosUpdate(request):    
    if request.method == "POST":
        #es un POST, por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla    
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        apellido_paterno=request.POST["apellido_paterno"]
        apellido_materno=request.POST["apellido_materno"]
        fecha_nacimiento=request.POST["fecha_nacimiento"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]

                
        objGenero=Genero.objects.get(id_genero=genero)

        usuario=Usuario()
        usuario.rut=rut
        usuario.nombre=nombre
        usuario.apellido_paterno=apellido_paterno
        usuario.apellido_materno=apellido_materno
        usuario.fecha_nacimiento=fecha_nacimiento
        usuario.id_genero=objGenero
        usuario.telefono=telefono
        usuario.email=email
        usuario.direccion=direccion

        usuario.activo=1
        usuario.save()

        generos=Genero.objects.all()
        context={'mensaje':"OK, datos actualizados...",'generos':generos, 'usuario':usuario}
        return render(request, 'venta/usuariosEdit.html', context)
    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios':usuarios}
        return render(request, 'venta/usuariosList.html', context)