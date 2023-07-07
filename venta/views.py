from django.contrib.auth.models import User

from .models import Perfil, Producto
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
import requests

import random
from django.views.decorators.csrf import csrf_protect
from .forms import LoginForm, RegisterForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.conf.urls.static import static
from django.utils import timezone
from .models import Producto
from .cart import Cart as Carrito
from .context_processor import cart_total_amount
from .forms import Prodform,ProdDes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.
def inicio(request):
    cart = Carrito(request)
    context = {}
    return render(request,'venta/index.html',context)

def sign(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'venta/formulario-sign-up.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            auth_login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'venta/formulario-sign-up.html', {'form': form})
 

# def login(request):    

#     return render(request, 'venta/formulario-login.html')

##API###

# def tienda(request):
#     Obtén el token de la API de Trefle
#     trefle_api_token = "Sr5y3wPL13rMLu5U4TGYAT-AK8R1ILIHckPS3NbQ2Fs"
    
#     URL de la solicitud
#     url = "https://trefle.io/api/v1/species/search"
    
#     Parámetros de la solicitud
#     rosa = {
#         "q": "Rosa chinensis",
#         "limit": 1,
#         "precio": 25.000
#     }

#     spreading = {
#         "q": "Spreading hedgeparsley",
#         "limit": 1,
#         "precio": 32.000
#     }    
    
#     Christmastree = {
#         "q": "Christmastree",
#         "limit": 1,
#         "precio": 55.000
#     }

#     cannabis = {
#         "q": "cannabis-sativa",
#         "limit": 1,
#         "precio": 20.000
#     }

#     clover = {
#         "q": "Cowgrass clover",
#         "limit": 1,
#         "precio": 15.000
#     }

#     Indian = {
#         "q": "Indian-dope",
#         "limit": 1,
#         "precio": 17.000
#     }    

#     Encabezados de la solicitud
#     headers = {
#         "Authorization": f"Bearer {trefle_api_token}"
#     }
    
#     Realiza la solicitud GET a la API de Trefle
#     response_rosa = requests.get(url, params=rosa, headers=headers)
#     response_spreading = requests.get(url, params=spreading, headers=headers)
#     response_Christmastree = requests.get(url, params=Christmastree, headers=headers)
#     response_cannabis = requests.get(url, params=cannabis, headers=headers)    
#     response_clover = requests.get(url, params=clover, headers=headers) 
#     response_Indian = requests.get(url, params=Indian, headers=headers) 

#     Obtén los datos de la respuesta en formato JSON
#     data_rosa = response_rosa.json()
#     data_spreading = response_spreading.json()
#     data_Christmastree = response_Christmastree.json()
#     data_cannabis = response_cannabis.json()
#     data_clover = response_clover.json()
#     data_Indian = response_Indian.json()

#     especies_rosa = data_rosa.get("data", [])
#     especies_spreading = data_spreading.get("data", [])
#     especies_Christmastree = data_Christmastree.get("data", [])
#     especies_cannabis = data_cannabis.get("data", [])
#     especies_clover = data_clover.get("data", [])
#     especies_Indian = data_Indian.get("data", [])

#     especies_totales = especies_rosa + especies_spreading + especies_Christmastree + especies_cannabis + especies_clover + especies_Indian

#     for especie in especies_totales:
#         especie["precio"] = generate_random_price()

#     return render(request, "venta/tienda.html", {"especies_totales": especies_totales, "especies_cannabis": especies_cannabis})

# def generate_random_price():
#     return random.randint(10000, 50000)



#CRUD#

def usuarios(request):
    return render(request,'venta/usuarios.html')

def usuariosList(request):
    #defino un objeto para trar el listado completo de usuarios desde la BD
    #Usuario.objects.all() <=> 'Select * From Usuario'
    usuarios= User.objects.all()
    perfiles = Perfil.objects.all()
    #cargo el objeto obtenido al contexto 
    context={
        'usuarios': usuarios,
        'perfiles' : perfiles
    }
    #agrego el contexto al retorno para que se vea en el template
    return render(request, 'venta/usuariosList.html', context)

def usuariosAdd(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'venta/usuariosAdd.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('usuariosList')
        else:
            return render(request, 'venta/usuarioAdd.html', {'form': form})
 
def usuariosDel(request, pk):
    
    usuario=User.objects.get(pk=pk)
    if usuario:
        usuario.delete()
        messages.success(request,'Usuario borrado exitosamente')
        return redirect('usuariosList')

    else:
        messages.error(request,'Error, no se pudo borrar el usuario')
        return redirect('usuariosList')

def usuariosEdit(request,pk):
    if pk != "":
        usuario=User.objects.get(pk=pk)
        perfil = Perfil.objects.get(user=usuario)

        context = {'usuario': usuario,'perfil':perfil}
        if usuario:
            return render (request,'venta/usuariosEdit.html',context)
        else:
            context={'mensaje': "Error, rut no existe..."}
            return render(request, 'venta/usuariosEdit.html', context)

def usuariosUpdate(request,pk):    
    if request.method == "POST":
        #es un POST, por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla    
        rut = request.POST['rut']
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        materno=request.POST["materno"]
        direccion=request.POST["telefono"]
        username=request.POST["username"]
        email=request.POST["email"]
        telefono=request.POST["telefono"]

        usuario=User.objects.get(pk=pk)

        perfil=Perfil.objects.get(user=usuario)
        perfil.rut = rut
        perfil.apellido_materno = materno
        perfil.direccion = direccion

        usuario.first_name=nombre
        usuario.last_name=apellido
        usuario.username=username
        usuario.email=email
        perfil.telefono=telefono

        usuario.save()
        perfil.save()
        messages.success(request,'Perfil actualizado correctamente')

        return redirect('usuariosList')
    else:
        usuarios = User.objects.all()
        perfiles = Perfil.objects.all()
        context = {'usuarios':usuarios,'perfiles':perfiles}
        return render(request, 'venta/usuariosList.html', context)
    

########################################



# @csrf_protect
# def index(request):
#     cart = Carrito(request)
#     return render(request, 'venta/inicio.html', {})

@csrf_protect
def tienda(request):
    products = Producto.objects.all()
    cart = Carrito(request)
    form = Prodform()
    if request.POST.get('marca'):
        if request.method == "POST":
            form = Prodform(request.POST, request.FILES)
            if form.is_valid():
                ProdAgre = form.save(commit=False)
                ProdAgre.nombre_producto = request.POST.get('nombre_producto')
                ProdAgre.imgProducto = form.cleaned_data['imgProducto']
                ProdAgre.save()
                return redirect('tienda')
    else:
            products = Producto.objects.all()
            return render(request, "venta/tienda.html", {
            "products": products,'form': form,})





@csrf_protect
def login(request):
    cart = Carrito(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                auth_login(request,user)
                messages.success(request,'Has iniciado sesión correctamente.')
                return redirect(reverse('inicio'))
        else:
            messages.error(request,'Usuario o contraseña incorrecta')
            return redirect(reverse('login'))
        
                
    else:
        form = LoginForm()
    return render(request,'venta/formulario-login.html',{'form':form})


@csrf_protect
def add_product_catalogo(request, product_id):
    cart = Carrito(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("/tienda.html")


def add_product_carrito(request, product_id):
    cart = Carrito(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("/carrito.html")

def productosList(request):
    productos = Producto.objects.all()
    #cargo el objeto obtenido al contexto 
    context={
        'productos' : productos
    }
    #agrego el contexto al retorno para que se vea en el template
    return render(request, 'venta/productosList.html', context)


@csrf_protect
def remove_product(request, product_id):
    cart = Carrito(request)
    product = Producto.objects.get(id=product_id)
    cart.remove(product)
    return redirect("/carrito.html")


@csrf_protect
def decrement_product(request, product_id):
    cart = Carrito(request)
    product = Producto.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("/carrito.html")


@csrf_protect
def clear_cart(request):
    cart = Carrito(request)
    cart.clear()
    return redirect("/carrito.html")

def producto_add(request):
    if request.method == 'POST':
        form = Prodform(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
           
            prod.save()
            messages.success(request, 'Producto creado correctamente')
            return redirect('productosList')
    form = Prodform()
    return render(request, 'venta/producto_add.html', {'form': form}) 

@csrf_protect
def modificar_producto(request, pk):
    cart = Carrito(request)
    prod = Producto.objects.get(id = pk)
    if request.method == 'POST':
        product = Prodform(request.POST, instance = prod)
        if product.is_valid():
            prod = product.save(commit=False)
            prod.save()
            return redirect('productosList')
    else:
        cart = Carrito(request)
        product = Prodform(instance= prod)    
        return render(request, 'venta/producto_edit.html',{'product':product})
    
@csrf_protect
def agregar_descuento(request, id):
    cart = Carrito(request)
    prod = Producto.objects.get(id = id)
    if request.method == 'POST':
        product = ProdDes(request.POST, instance = prod)
        if product.is_valid():
            prod = product.save(commit=False)
            prod.save()
            return redirect('tienda.html')
    else:
        cart = Carrito(request)
        product = ProdDes(instance= prod)    
        return render(request, 'venta/producto_desc.html',{'product':product,'prod':prod})
       
@csrf_protect
def eliminar_producto(request, id):
    cart = Carrito(request)
    product = Producto.objects.get(id=id)
    try:
        product.delete()
        mensajes = "Eliminado correctamente"
        messages.success(request, mensajes)
        return redirect('productosList')
    except:
        cart = Carrito(request)
        mensaje = "No se a eliminado el archivo seleccionado"
        messages.error(request, mensaje)
    return redirect('productosList')
 
def carrito(request):
    cart = Carrito(request)
    total = 0
    FprecioC = 0
    total = 0
    FprecioC = 0
    if request.user.is_authenticated:
        for key, value in request.session['carrito'].items():
            total = total + (float(value['price']) * value['quantity'])
            
            FprecioC= int(total)
            if request.method == "POST":
                messages.success(request,'Pago ingresado con exito')

                return redirect('index.html')
            
    amount = FprecioC
    return render(request, 'venta/carrito.html', {})