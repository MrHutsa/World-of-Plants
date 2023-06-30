from django.contrib import admin

from .models import Usuario, Perfil, categoria, subcategoria, Producto, descuento
admin.site.register(Perfil)

# Register your models here.
#admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(categoria)
admin.site.register(subcategoria)

admin.site.register(descuento)