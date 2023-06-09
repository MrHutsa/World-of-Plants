from django.urls import path

from .views import inicio, tienda, sign, login

urlpatterns = [
    path("", inicio,name ='inicio'),
    path("tienda", tienda,name="tienda"),
    path("formulario-sign-up.html", sign,name="sign"),
    path("formula-login.html", login,name="login"),
]