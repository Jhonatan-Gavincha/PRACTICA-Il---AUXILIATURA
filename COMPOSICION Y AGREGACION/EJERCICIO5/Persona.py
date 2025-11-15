class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} (CI: {self.ci})"

class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad
    
    def __str__(self):
        return f"Speaker: {self.nombre} {self.apellido} - Especialidad: {self.especialidad}"

class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket
    
    def __str__(self):
        return f"Participante: {self.nombre} {self.apellido} - Ticket: {self.nroTicket}"

class Charla:
    def __init__(self, lugar, nombre_charla, speaker):
        self.lugar = lugar
        self.nombre_charla = nombre_charla
        self.s = speaker  # Speaker
        self.np = 0  # Número de participantes
        self.P = [None] * 50  # Array de participantes (máximo 50)
    
    def agregar_participante(self, participante):
        if self.np < 50:
            self.P[self.np] = participante
            self.np += 1
            return True
        return False
    
    def eliminar_speaker(self):
        """Elimina el speaker de esta charla"""
        self.s = None
    
    def tiene_speaker(self):
        """Verifica si la charla tiene speaker asignado"""
        return self.s is not None
    
    def obtener_participantes(self):
        """Retorna lista de participantes (sin None)"""
        return [p for p in self.P if p is not None]
    
    def __str__(self):
        speaker_info = self.s.nombre if self.s else "Sin speaker"
        return f"Charla: {self.nombre_charla} - Lugar: {self.lugar} - Speaker: {speaker_info} - Participantes: {self.np}"

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nc = 0  # Número de charlas
        self.C = [None] * 50  # Array de charlas (máximo 50)
    
    def agregar_charla(self, charla):
        if self.nc < 50:
            self.C[self.nc] = charla
            self.nc += 1
            return True
        return False
    
    def edad_promedio_participantes(self):
        total_edad = 0
        total_participantes = 0
        
        for i in range(self.nc):
            charla = self.C[i]
            if charla:
                for participante in charla.obtener_participantes():
                    total_edad += participante.edad
                    total_participantes += 1
        
        if total_participantes == 0:
            return 0
        return total_edad / total_participantes
    
    # b) Verificar si persona está en alguna charla como participante o speaker
    def buscar_persona(self, nombre, apellido):
        for i in range(self.nc):
            charla = self.C[i]
            if charla:
                # Buscar como speaker
                if charla.s and charla.s.nombre == nombre and charla.s.apellido == apellido:
                    return f"Encontrado como SPEAKER en: {charla.nombre_charla}"
                
                # Buscar como participante
                for participante in charla.obtener_participantes():
                    if participante.nombre == nombre and participante.apellido == apellido:
                        return f"Encontrado como PARTICIPANTE en: {charla.nombre_charla}"
        
        return f"Persona {nombre} {apellido} no encontrada en el evento"
    
    # c) Eliminar charlas de speaker con CI específico
    def eliminar_charlas_por_speaker(self, ci_speaker):
        charlas_eliminadas = 0
        # Primero marcamos las charlas para eliminar (ponemos None)
        for i in range(self.nc):
            if self.C[i] and self.C[i].s and self.C[i].s.ci == ci_speaker:
                self.C[i] = None
                charlas_eliminadas += 1
        
        # Reorganizamos el array para eliminar los None
        if charlas_eliminadas > 0:
            nuevas_charlas = [charla for charla in self.C if charla is not None]
            # Limpiamos el array original
            self.C = [None] * 50
            # Volvemos a llenar
            for j in range(len(nuevas_charlas)):
                self.C[j] = nuevas_charlas[j]
            self.nc = len(nuevas_charlas)
        
        return charlas_eliminadas
    
    # d) Ordenar charlas por número de participantes
    def ordenar_charlas_por_participantes(self):
        # Filtramos charlas existentes y ordenamos
        charlas_existentes = [charla for charla in self.C if charla is not None]
        charlas_ordenadas = sorted(charlas_existentes, key=lambda x: x.np, reverse=True)
        
        # Actualizamos el array
        self.C = [None] * 50
        for i in range(len(charlas_ordenadas)):
            self.C[i] = charlas_ordenadas[i]
        self.nc = len(charlas_ordenadas)
    
    def mostrar_charlas(self):
        print(f"\n--- Charlas del Evento: {self.nombre} ---")
        for i in range(self.nc):
            if self.C[i]:
                print(f"{i+1}. {self.C[i]}")
    
    def mostrar_detalle_charlas(self):
        print(f"\n--- Detalle Completo del Evento: {self.nombre} ---")
        for i in range(self.nc):
            charla = self.C[i]
            if charla:
                print(f"\n{i+1}. {charla}")
                if charla.s:
                    print(f"   Speaker: {charla.s}")
                print(f"   Participantes ({charla.np}):")
                for participante in charla.obtener_participantes():
                    print(f"     - {participante}")

# DEMOSTRACIÓN DEL SISTEMA
def demostrar_sistema():
    print("=== SISTEMA DE EVENTOS Y CHARLAS ===\n")
    
    # Crear speakers
    speaker1 = Speaker("Ana", "García", 35, 1234567, "Inteligencia Artificial")
    speaker2 = Speaker("Carlos", "López", 42, 7654321, "Ciberseguridad")
    speaker3 = Speaker("María", "Rodríguez", 38, 9876543, "Blockchain")
    
    # Crear participantes
    participante1 = Participante("Juan", "Pérez", 25, 1111111, 1001)
    participante2 = Participante("Laura", "Martínez", 30, 2222222, 1002)
    participante3 = Participante("Pedro", "Sánchez", 28, 3333333, 1003)
    participante4 = Participante("Sofia", "Ramírez", 32, 4444444, 1004)
    participante5 = Participante("Diego", "Fernández", 26, 5555555, 1005)
    
    # Crear charlas
    charla1 = Charla("Auditorio A", "Introducción a IA", speaker1)
    charla2 = Charla("Sala B", "Seguridad Informática", speaker2)
    charla3 = Charla("Auditorio Principal", "Blockchain en Finanzas", speaker3)
    
    # Agregar participantes a charlas
    charla1.agregar_participante(participante1)
    charla1.agregar_participante(participante2)
    charla1.agregar_participante(participante3)
    
    charla2.agregar_participante(participante2)
    charla2.agregar_participante(participante4)
    
    charla3.agregar_participante(participante1)
    charla3.agregar_participante(participante3)
    charla3.agregar_participante(participante5)
    
    evento = Evento("Conferencia de Tecnología 2024")
    evento.agregar_charla(charla1)
    evento.agregar_charla(charla2)
    evento.agregar_charla(charla3)
    
    evento.mostrar_detalle_charlas()
    
    print(f"\n=== a) EDAD PROMEDIO DE PARTICIPANTES ===")
    promedio = evento.edad_promedio_participantes()
    print(f"Edad promedio de todos los participantes: {promedio:.2f} años")
    
    print(f"\n=== b) BÚSQUEDA DE PERSONAS ===")
    print(evento.buscar_persona("Ana", "García"))      # Speaker
    print(evento.buscar_persona("Juan", "Pérez"))      # Participante
    print(evento.buscar_persona("Luis", "González"))   # No existe
    
    print(f"\n=== c) ELIMINAR CHARLAS DE SPEAKER ===")
    ci_a_eliminar = 7654321  # Carlos López
    eliminadas = evento.eliminar_charlas_por_speaker(ci_a_eliminar)
    print(f"Se eliminaron {eliminadas} charlas del speaker con CI: {ci_a_eliminar}")
    evento.mostrar_charlas()
    
    print(f"\n=== d) ORDENAR CHARLAS POR PARTICIPANTES ===")
    print("Antes de ordenar:")
    evento.mostrar_charlas()
    
    evento.ordenar_charlas_por_participantes()
    
    print("\nDespués de ordenar (mayor a menor participantes):")
    evento.mostrar_charlas()

demostrar_sistema()