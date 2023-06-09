from django.shortcuts import render
from django.http import JsonResponse

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