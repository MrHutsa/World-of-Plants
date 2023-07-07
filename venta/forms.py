from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Nombre de usuario',
                'class' : 'form-control form-control-lg',
                'id' : 'typeEmailX'
            }
        )
    )

    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
                'class' : 'form-control form-control-lg',
                'id' : 'typePasswordX'
            }
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Nombre de usuario',
                'class' : 'form-control form-control-lg',
                'id' : 'typeEmailX'
            }
        )
    )
    email = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Nombre de usuario',
                'class' : 'form-control form-control-lg',
                'id' : 'typeEmailX'
            }
        )
    )

    password1 = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
                'class' : 'form-control form-control-lg',
                'id' : 'typePasswordX'
            }
        )
    )
    password2 = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
                'class' : 'form-control form-control-lg',
                'id' : 'typePasswordX'
            }
        )
    )
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

class Prodform(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre_producto','precio','imgProducto','descuento')

class ProdDes(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descuento',)