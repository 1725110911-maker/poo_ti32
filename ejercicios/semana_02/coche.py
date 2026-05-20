class Coche:
    def __init__ (self, año, modelo, capacidad_de_carga, 
        tipo_de_combustible, motor, color, placas, 
        kilometraje, potencia_de_motor, marca):
        self.año = año
        self.modelo = modelo
        self.capacidad_de_carga = capacidad_de_carga
        self.tipo_de_combustible = tipo_de_combustible
        self.motor = motor
        self.color = color
        self.placas = placas
        self.kilometraje = kilometraje
        self.potencia_de_motor = potencia_de_motor
        self.marca = marca
        print(f"Año:{self.año}")
        print(f"Modelo:{self.modelo}")
        print(f"Capacidad de carga:{self.capacidad_de_carga}")
        print(f"Tipo de combustible:{self.tipo_de_combustible}")
        print(f"Motor:{self.motor}")
        print(f"Color:{self.color}")
        print(f"Placas:{self.placas}")
        print(f"Kilometraje:{self.kilometraje}")
        print(f"Potencia de motor:{self.potencia_de_motor}")
        print(f"Marca :{self.marca}")
    def encender(self):
        print("Camion enciende")
    def acelerar(self):
        print("Camion acelera")
    def frenar(self):
        print("Camion frena")
    def aireAcondicionado(self):
        print("Aire acondicionado")
    def cajuela(self):
        print("Cajuela")

nissan_versa = Coche("2024", "versa", "500 kg", "Gasolina", 
        "1.6 L 4 cilindros", "Gris platino", "HRV-20-26", "5400 kilometros",
        "118 hp", "Nissan")
nissan_versa.acelerar()
nissan_versa.encender()
nissan_versa.frenar()
nissan_versa.aireAcondicionado()
nissan_versa.cajuela()