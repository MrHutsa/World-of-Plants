class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def __str__(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }

        else:
            self.carrito[id]["cantidad"]  += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified   = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified   = True

from django import template
register = template.Library()

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def add(self, product):
        if str(product.id) not in self.carrito.keys():
            self.carrito[product.id] = {
                "product_id": product.id,
                "name": product.nombre_producto,
                "quantity": 1,
                "price": str( product.precio-(product.precio*(product.descuento.descuento/100))),
                "image": product.imgProducto.url,           
                "desc": product.descuento.descuento

            }
        else:
            for key, value in self.carrito.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    break
        self.save()

    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.carrito:
            del self.carrito[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.carrito.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.remove(product)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")

    def clear(self):
        self.session["carrito"] = {}
        self.session.modified = True
