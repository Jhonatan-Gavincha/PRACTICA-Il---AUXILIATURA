# Excepciones personalizadas
class ProductoNoEncontradoException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class StockInsuficienteException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class CodigoExistenteException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


# Clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}) - Precio: ${self.precio} - Stock: {self.stock}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # c) Agregar producto
    def agregar_producto(self, producto: Producto):
        # Verificar si código ya existe
        for p in self.productos:
            if p.codigo == producto.codigo:
                raise CodigoExistenteException(f"El código '{producto.codigo}' ya existe")
        # Verificar precio y stock
        if producto.precio < 0 or producto.stock < 0:
            raise ValueError("Precio y stock deben ser mayores o iguales a 0")
        self.productos.append(producto)

    # d) Buscar producto
    def buscar_producto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        raise ProductoNoEncontradoException(f"Producto con código '{codigo}' no encontrado")

    # e) Vender producto
    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {producto.nombre}")
        else:
            raise StockInsuficienteException(f"Stock insuficiente para {producto.nombre}. Disponible: {producto.stock}")

    # Mostrar inventario
    def mostrar_inventario(self):
        print("=== Inventario ===")
        for p in self.productos:
            print(f" - {p}")


# -----------------------------
# Ejemplo de uso
# -----------------------------
inventario = Inventario()

# Agregar productos
try:
    inventario.agregar_producto(Producto("P001", "Laptop", 1500, 10))
    inventario.agregar_producto(Producto("P002", "Mouse", 20, 50))
    inventario.agregar_producto(Producto("P003", "Teclado", 35, 30))
except Exception as e:
    print(e)

# Mostrar inventario
inventario.mostrar_inventario()

# Intentar vender
try:
    inventario.vender_producto("P002", 5)
    inventario.vender_producto("P003", 40)  # Stock insuficiente
except Exception as e:
    print(e)

# Buscar producto
try:
    prod = inventario.buscar_producto("P005")  # No existe
except Exception as e:
    print(e)

# Intentar agregar producto con código repetido
try:
    inventario.agregar_producto(Producto("P001", "Tablet", 300, 15))
except Exception as e:
    print(e)

# Intentar agregar producto con precio negativo
try:
    inventario.agregar_producto(Producto("P004", "Monitor", -50, 5))
except Exception as e:
    print(e)
