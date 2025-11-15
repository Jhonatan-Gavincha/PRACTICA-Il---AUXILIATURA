class Bailarin:
    def __init__(self, nombre, edad, facultad=None, fraternidad=None):
        self.nombre = nombre
        self.edad = edad
        self.facultad = facultad
        self.fraternidad = fraternidad
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, Facultad: {self.facultad.nombre if self.facultad else 'N/A'}, Fraternidad: {self.fraternidad.nombre if self.fraternidad else 'N/A'}"

class Fraternidad:
    def __init__(self, nombre, encargado=None):
        self.nombre = nombre
        self.encargado = encargado
        self.bailarines = []
    
    def agregar_bailarin(self, bailarin):
        if bailarin.fraternidad:
            print(f"{bailarin.nombre} ya pertenece a otra fraternidad.")
        else:
            bailarin.fraternidad = self
            self.bailarines.append(bailarin)

class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bailarines = []
    
    def agregar_bailarin(self, bailarin):
        bailarin.facultad = self
        self.bailarines.append(bailarin)

facultad1 = Facultad("Ingeniería")
facultad2 = Facultad("Arquitectura")

frat1 = Fraternidad("Alpha", encargado=None)
frat2 = Fraternidad("Beta", encargado=None)

b1 = Bailarin("Ana", 20)
b2 = Bailarin("Luis", 22)
b3 = Bailarin("Carla", 21)
b4 = Bailarin("Diego", 23)
b5 = Bailarin("Sofía", 19)

frat1.encargado = b1
frat2.encargado = b4

frat1.agregar_bailarin(b1)
frat1.agregar_bailarin(b2)
frat2.agregar_bailarin(b3)
frat2.agregar_bailarin(b4)
frat2.agregar_bailarin(b5)

facultad1.agregar_bailarin(b1)
facultad1.agregar_bailarin(b3)
facultad1.agregar_bailarin(b5)
facultad2.agregar_bailarin(b2)
facultad2.agregar_bailarin(b4)

print("=== Bailarines registrados ===")
for b in [b1, b2, b3, b4, b5]:
    print(b)

print("\n=== Fraternidades y encargados ===")
for f in [frat1, frat2]:
    print(f"{f.nombre} - Encargado: {f.encargado.nombre}")
    for b in f.bailarines:
        print(f"  {b.nombre}")

print("\n=== Facultades y bailarines ===")
for fac in [facultad1, facultad2]:
    print(f"{fac.nombre}:")
    for b in fac.bailarines:
        print(f"  {b.nombre}")
