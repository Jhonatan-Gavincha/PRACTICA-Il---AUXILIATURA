class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
    
    def __str__(self):
        return f"{self.nombre} - {self.cargo} - ${self.sueldo:,.2f}"

class Departamento:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.empleados = []  # Lista para almacenar empleados
    
    def agregar_empleado(self, empleado):
        """Agrega un empleado al departamento"""
        self.empleados.append(empleado)
    
    def mostrar_empleados(self):
        """Muestra todos los empleados del departamento"""
        print(f"\n--- Empleados del Departamento {self.nombre} ({self.area}) ---")
        if not self.empleados:
            print("No hay empleados en este departamento")
        else:
            for i, empleado in enumerate(self.empleados, 1):
                print(f"{i}. {empleado}")
    
    def cambiar_salario(self, porcentaje):
        """Cambia el salario de todos los empleados del departamento"""
        for empleado in self.empleados:
            empleado.sueldo *= (1 + porcentaje / 100)
        print(f"Salarios actualizados en {porcentaje}% para el departamento {self.nombre}")
    
    def tiene_empleado(self, empleado):
        """Verifica si un empleado pertenece a este departamento"""
        return empleado in self.empleados
    
    def mover_empleados_a(self, otro_departamento):
        """Mueve todos los empleados de este departamento a otro"""
        if self.empleados:
            print(f"\nMoviendo {len(self.empleados)} empleados de {self.nombre} a {otro_departamento.nombre}")
            otro_departamento.empleados.extend(self.empleados)
            self.empleados.clear()
        else:
            print(f"\nNo hay empleados para mover del departamento {self.nombre}")

print("=== a) INSTANCIACIÓN DE DEPARTAMENTOS ===")

departamento1 = Departamento("Ventas", "Comercial")

empleados_dep1 = [
    Empleado("Ana García", "Gerente de Ventas", 50000),
    Empleado("Carlos López", "Ejecutivo de Ventas", 35000),
    Empleado("María Rodríguez", "Asistente de Ventas", 30000),
    Empleado("Pedro Martínez", "Representante", 28000),
    Empleado("Laura Fernández", "Coordinadora", 32000)
]

for empleado in empleados_dep1:
    departamento1.agregar_empleado(empleado)

departamento2 = Departamento("Marketing", "Comunicaciones")

print(f"Departamento 1 creado: {departamento1.nombre}")
print(f"Departamento 2 creado: {departamento2.nombre}")

print("\n=== b) MOSTRAR EMPLEADOS ===")
departamento1.mostrar_empleados()
departamento2.mostrar_empleados()

print("\n=== c) CAMBIO DE SALARIO ===")
print("Salarios antes del aumento:")
departamento1.mostrar_empleados()

departamento1.cambiar_salario(10)

print("Salarios después del aumento:")
departamento1.mostrar_empleados()

print("\n=== d) VERIFICACIÓN DE EMPLEADOS ===")
empleado_verificar = empleados_dep1[0] 
pertenece = departamento2.tiene_empleado(empleado_verificar)
print(f"¿El empleado {empleado_verificar.nombre} pertenece al departamento {departamento2.nombre}? {pertenece}")

print(f"\nVerificando todos los empleados del departamento 1 en el departamento 2:")
for empleado in departamento1.empleados:
    pertenece = departamento2.tiene_empleado(empleado)
    print(f"{empleado.nombre}: {pertenece}")

print("\n=== e) MOVER EMPLEADOS ===")
print("Antes de mover:")
departamento1.mostrar_empleados()
departamento2.mostrar_empleados()

departamento1.mover_empleados_a(departamento2)

print("Después de mover:")
departamento1.mostrar_empleados()
departamento2.mostrar_empleados()