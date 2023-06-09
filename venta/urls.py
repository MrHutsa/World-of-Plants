from django.urls import path

from .views import inicio, tienda, sign, login
from . import views

urlpatterns = [
    path("", inicio,name ='inicio'),
    path("tienda", tienda,name="tienda"),
    path("formulario-sign-up.html", sign,name="sign"),
    path("formula-login.html", login,name="login"),

    #CRUD
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuariosList', views.usuariosList, name='usuariosList'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    path('usuariosDel/<str:pk>', views.usuariosDel, name='usuariosDel'),
    path('usuariosEdit/<str:pk>', views.usuariosEdit, name='usuariosEdit'),
    path('usuariosUpdate', views.usuariosUpdate, name='usuariosUpdate'),
]