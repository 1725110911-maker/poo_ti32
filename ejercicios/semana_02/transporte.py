class Transporte:
    def __init__ (self, marca, modelo, capacidad_de_carga, 
        tipo_de_combustible, numero_de_eje, color, placas, 
        kilometraje, potencia_de_motor, empresa_propietaria):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_de_carga = capacidad_de_carga
        self.tipo_de_combustible = tipo_de_combustible
        self.numero_de_eje = numero_de_eje
        self.color = color
        self.placas = placas
        self.kilometraje = kilometraje
        self. potencia_de_motor = potencia_de_motor
        self.empresa_propietaria = empresa_propietaria
        print(f"Marca :{self.marca}")
        print(f"Modelo:{self.modelo}")
        print(f"Capacidad de carga:{self.capacidad_de_carga}")
        print(f"Tipo de combustible:{self.tipo_de_combustible}")
        print(f"Numero de eje:{self.numero_de_eje}")
        print(f"Color:{self.color}")
        print(f"Placas:{self.placas}")
        print(f"Kilometraje:{self.kilometraje}")
        print(f"Potencia de motor:{self.potencia_de_motor}")
        print(f"Empresa propietaria:{self.empresa_propietaria}")
    def encender(self):
        print("Camion enciende")
    def acelerar(self):
        print("Camion acelera")
    def frenar(self):
        print("Camion frena")
    def cargarMercancia(self):
        print("Carga de mercancia")
    def tocarClaxon(self):
        print("¡BEEP BEEP!")

coche = Transporte ("kenworth", "t680", "0.5", "Diesel", 
        "3 ejes", "Blanco", "ABC-123", "50000 kilometros",
        "450 hp", "Transportes Mexico")
coche.acelerar()
coche.encender()
coche.frenar()
coche. cargarMercancia()
coche.tocarClaxon()