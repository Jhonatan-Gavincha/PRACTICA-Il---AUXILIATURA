class Medicamento:
    def __init__(self, nombre, principio_activo, precio, fecha_vencimiento):
        self.nombre = nombre
        self.principio_activo = principio_activo
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento
    
    def __str__(self):
        return f"{self.nombre} ({self.principio_activo}) - ${self.precio}"

class Laboratorio:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.medicamentos_producidos = []  # Composicion
    
    def agregar_medicamento(self, medicamento):
        self.medicamentos_producidos.append(medicamento)
    
    def __str__(self):
        return f"Laboratorio: {self.nombre}"

class Farmacia:
    def __init__(self, nombre, direccion, horario_atencion):
        self.nombre = nombre
        self.direccion = direccion
        self.horario_atencion = horario_atencion
        self.inventario = []  # Agregacion
        self.empleados = []   # Agregacion
    
    def agregar_medicamento_inventario(self, medicamento):
        self.inventario.append(medicamento)
    
    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def mostrar_inventario(self):
        print(f"\n--- Inventario de {self.nombre} ---")
        for med in self.inventario:
            print(f"- {med}")

class Empleado:
    def __init__(self, nombre, cargo, salario, turno):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.turno = turno
        self.farmacia_trabajo = None  # Asociacion
    
    def asignar_farmacia(self, farmacia):
        self.farmacia_trabajo = farmacia
    
    def __str__(self):
        return f"{self.nombre} - {self.cargo} (Turno: {self.turno})"

class Cliente:
    def __init__(self, nombre, dni, seguro_medico):
        self.nombre = nombre
        self.dni = dni
        self.seguro_medico = seguro_medico
        self.recetas = []  # Composicion
    
    def agregar_receta(self, receta):
        self.recetas.append(receta)
    
    def __str__(self):
        return f"Cliente: {self.nombre} (DNI: {self.dni})"

class Receta:
    def __init__(self, numero_receta, fecha_emision, medico):
        self.numero_receta = numero_receta
        self.fecha_emision = fecha_emision
        self.medico = medico
        self.medicamentos_recetados = []  # Agregacion
    
    def agregar_medicamento(self, medicamento):
        self.medicamentos_recetados.append(medicamento)
    
    def __str__(self):
        return f"Receta #{self.numero_receta} - Dr. {self.medico}"

class Venta:
    def __init__(self, numero_venta, fecha, total):
        self.numero_venta = numero_venta
        self.fecha = fecha
        self.total = total
        self.medicamentos_vendidos = []  # Agregacion
        self.cliente = None              # Asociacion
        self.empleado = None             # Asociacion
    
    def agregar_medicamento_venta(self, medicamento):
        self.medicamentos_vendidos.append(medicamento)
    
    def asignar_cliente(self, cliente):
        self.cliente = cliente
    
    def asignar_empleado(self, empleado):
        self.empleado = empleado
    
    def __str__(self):
        return f"Venta #{self.numero_venta} - Total: ${self.total}"

# Ejemplo de uso y demostración
def demostrar_sistema_farmacia():
    print("=== SISTEMA DE FARMACIA ===\n")
    
    # 1. Crear Laboratorio (Composición con Medicamento)
    lab_pfizer = Laboratorio("Pfizer", "Av. Principal 123", "555-1234")
    
    # 2. Crear Medicamentos (Composición del Laboratorio)
    medicamento1 = Medicamento("Aspirina", "Ácido Acetilsalicílico", 15.50, "2025-12-31")
    medicamento2 = Medicamento("Amoxicilina", "Amoxicilina Trihidrato", 45.80, "2024-10-15")
    
    lab_pfizer.agregar_medicamento(medicamento1)
    lab_pfizer.agregar_medicamento(medicamento2)
    
    farmacia_del_centro = Farmacia("Farmacia Central", "Calle Principal 456", "08:00-22:00")
    
    farmacia_del_centro.agregar_medicamento_inventario(medicamento1)
    farmacia_del_centro.agregar_medicamento_inventario(medicamento2)
    
    empleado1 = Empleado("María González", "Farmacéutico", 2500, "Mañana")
    empleado2 = Empleado("Carlos Ruiz", "Cajero", 1800, "Tarde")
    
    farmacia_del_centro.contratar_empleado(empleado1)
    farmacia_del_centro.contratar_empleado(empleado2)
    
    empleado1.asignar_farmacia(farmacia_del_centro)
    empleado2.asignar_farmacia(farmacia_del_centro)
    
    cliente1 = Cliente("Ana López", "12345678A", "Seguro Salud Plus")
    
    receta1 = Receta("R-2024-001", "2024-01-15", "Dr. Rodríguez")
    receta1.agregar_medicamento(medicamento1)
    
    cliente1.agregar_receta(receta1)
    
    venta1 = Venta("V-2024-001", "2024-01-15", 61.30)
    venta1.agregar_medicamento_venta(medicamento1)
    venta1.agregar_medicamento_venta(medicamento2)
    venta1.asignar_cliente(cliente1)
    venta1.asignar_empleado(empleado1)
    
    print("1. LABORATORIO Y MEDICAMENTOS:")
    print(f"   {lab_pfizer}")
    for med in lab_pfizer.medicamentos_producidos:
        print(f"   - {med}")
    
    print("\n2. FARMACIA:")
    print(f"   {farmacia_del_centro.nombre}")
    print(f"   Dirección: {farmacia_del_centro.direccion}")
    
    print("\n3. EMPLEADOS:")
    for emp in farmacia_del_centro.empleados:
        print(f"   {emp}")
    
    print("\n4. INVENTARIO:")
    farmacia_del_centro.mostrar_inventario()
    
    print("\n5. CLIENTE Y RECETA:")
    print(f"   {cliente1}")
    for receta in cliente1.recetas:
        print(f"   {receta}")
        for med in receta.medicamentos_recetados:
            print(f"     - {med}")
    
    print("\n6. VENTA REALIZADA:")
    print(f"   {venta1}")
    print(f"   Cliente: {venta1.cliente.nombre}")
    print(f"   Empleado: {venta1.empleado.nombre}")

# Ejecutar demostración
demostrar_sistema_farmacia()