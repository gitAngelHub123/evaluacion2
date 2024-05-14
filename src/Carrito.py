class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
        
    def add(self, product):
        id = str(product.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                
                "product_id": product.id,
                "name": product.name,
                "quantity": 1,
                "price": product.price,  # Asegúrate de que el precio sea un tipo de dato numérico
                "image": product.image.url
        }
        else:
            self.carrito[id]["quantity"] += 1
            self.carrito[id]["price"] += product.price
        self.guardar_carrito()


        
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def remove(self, product):
        id = str(product.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
            
    def restar(self, product):
        id = str(product.id)
        if id in self.carrito.keys():
            self.carrito[id]["quantity"] -= 1
            self.carrito[id]["price"] -= product.price
            if self.carrito[id]["quantity"] <= 0: self.remove(product)
            self.guardar_carrito()
                
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True 