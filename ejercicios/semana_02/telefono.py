class Telefono:
    def __init__ (self, procesador, memoriaram, almacenamiento, 
            pantalla, bateria, camara, sistema_operativo,
            conectividad, material, sensores):
        self.procesaror = procesador
        self.memoriaRam = memoriaram
        self.almacenamiento = almacenamiento
        self.pantalla = pantalla
        self.bateria = bateria
        self.camara = camara
        self.sistema_operativo = sistema_operativo
        self.conectividad = conectividad
        self.material = material
        self.sensores = sensores
        print(f" Procesaror:{self.procesaror}")
        print(f"Memoria RAM:{self.memoriaRam}")
        print(f"Almacenamiento:{self.almacenamiento}")
        print(f"Pantalla:{self.pantalla}")
        print(f"Bateria:{self.bateria}")
        print(f"Camara:{self.camara}")
        print(f"Sistema operativo:{self.sistema_operativo}")
        print(f"Conectividad:{self.conectividad}")
        print(f"Material:{self.material}")
        print(f"Sensores:{self.sensores}")

poo_m5s = Telefono("Media tek helio G96", "4GB/6GB", "6.43`` AMOLED Dont display",
    "64 GB/128GB UFS 2.2.", "5000 mAh con carga rapida", 
    "cuadruple sensor principal de 64 MP", "MIUI 13 basado em android 12",
    "4G LTE", "Policarbonato", "Huella dactilar e IA de desbloqueo")
