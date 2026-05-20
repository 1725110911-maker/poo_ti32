class Perro:
    def __init__(self, nombre, raza, edad, color, peso, tamaño, 
    entrenador, nom_dueño, nivel_energia, todas_vacunas):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso
        self.tamaño = tamaño
        self.entrenador = entrenador
        self.nom_dueño = nom_dueño
        self.nivel_energia = nivel_energia
        self.todas_vacunas = todas_vacunas
        print(f"{self.nombre}")
        print(f"{self.raza}")
        print(f"{self.edad}")
        print(f"{self.color}")
        print(f"{self.peso}")
        print(f"{self.tamaño}")
        print(f"{self.entrenador}")
        print(f"{self.nom_dueño}")
        print(f"{self.nivel_energia}")
        print(f"{self.todas_vacunas}")

    def jugar(self):
        print("juega")
    def ladrar(self):
        print("GUAF")
    def morder(self):
        print("AUCH")
    def comer(self):
        print("yam yam")
    def dormir(self):
        print("Zzzzzzz")

borderCollie = Perro("Max", "Border Collie", "3 años", "Blanco con negro", 
    "19 kilogramos", "Mediano", "Carlos Mendoza", "Valeria Sofía Silva", 
    "Muy alto", "Si")

borderCollie.jugar()
borderCollie.ladrar()
borderCollie.morder()
borderCollie.comer()
borderCollie.dormir()