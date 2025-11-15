class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} - {self.puesto} - ${self.salario}"


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  # agregación

    # a) Agregar empleado
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    # b) Mostrar información de empresa y empleados
    def mostrar_informacion(self):
        print(f"Empresa: {self.nombre}")
        print("Empleados:")
        for e in self.empleados:
            print(f" - {e}")

    # c) Buscar empleado por nombre
    def buscar_empleado(self, nombre):
        for e in self.empleados:
            if e.nombre.lower() == nombre.lower():
                return e
        return None

    # d) Eliminar empleado por nombre
    def eliminar_empleado(self, nombre):
        for e in self.empleados:
            if e.nombre.lower() == nombre.lower():
                self.empleados.remove(e)
                return True
        return False

    # e) Promedio salarial
    def promedio_salarial(self):
        if not self.empleados:
            return 0
        total = sum(e.salario for e in self.empleados)
        return total / len(self.empleados)

    # Empleados con salario mayor a un valor dado
    def listar_mayor_salario(self, valor):
        print(f"Empleados con salario mayor a ${valor}:")
        for e in self.empleados:
            if e.salario > valor:
                print(f" - {e}")


# -------------------------
# Ejemplo de uso
# -------------------------
empresa = Empresa("Tech Solutions")

# a) Agregar empleados
empresa.agregar_empleado(Empleado("Ana Pérez", "Programadora", 2500))
empresa.agregar_empleado(Empleado("Luis Gómez", "Analista", 2800))
empresa.agregar_empleado(Empleado("Carla Ruiz", "Diseñadora", 2200))
empresa.agregar_empleado(Empleado("Diego Fernández", "Gerente", 4000))

# b) Mostrar información
empresa.mostrar_informacion()

# c) Buscar empleado
print("\nBuscando empleado Luis Gómez:")
buscado = empresa.buscar_empleado("Luis Gómez")
if buscado:
    print(f"Encontrado: {buscado}")
else:
    print("No encontrado")

# d) Eliminar empleado
print("\nEliminando empleado Carla Ruiz...")
empresa.eliminar_empleado("Carla Ruiz")
empresa.mostrar_informacion()

# e) Promedio salarial
print(f"\nPromedio salarial: ${empresa.promedio_salarial():.2f}")

# Empleados con salario mayor a 3000
empresa.listar_mayor_salario(3000)
