from django.urls import path , include
from django.contrib.auth.views import LoginView , LogoutView
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("", views.inicio,name ='inicio'),
    path('index.html', views.inicio, name='inicio'),
    path("tienda.html", views.tienda,name="tienda"),
    path('formulario-sign-up.html', views.sign,name="sign"),

    path("carrito.html", views.carrito,name="carrito"),

    path('login',views.login, name="login"),
    path('logout',LogoutView.as_view(template_name = 'venta/inicio.html'), name="logout"),


    path('usuarios.html', views.usuarios, name='usuarios'),
    path('usuariosList.html', views.usuariosList, name='usuariosList'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    path('usuariosDel/<str:pk>', views.usuariosDel, name='usuariosDel'),
    path('usuariosEdit/<str:pk>', views.usuariosEdit, name='usuariosEdit'),
    path('usuariosUpdate/<str:pk>', views.usuariosUpdate, name='usuariosUpdate'),

    path('productosList.html', views.productosList, name='productosList'),
    path('producto_add', views.producto_add, name='producto_add' ),

    path('add_product_carrito/<int:product_id>/', add_product_carrito, name='add_product_carrito'),
    path('add_product_catalogo/<int:product_id>/', add_product_catalogo, name='add_product_catalogo'),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
    path('decrement_product/<int:product_id>/', decrement_product, name='decrement_product'),
    path('producto_edit.html/<int:pk>/', modificar_producto, name="modificar_producto"),
    path('agregar_descuento.html/<id>/', agregar_descuento, name="agregar_descuento"),
    path('eliminar-producto/<int:id>/', eliminar_producto, name="eliminar_producto"),
    path('clear/', clear_cart, name='clear_cart'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)