class Personaje:

    def __init__(self, nombre, nivel, vida, energia, fuerza, 
        defenza, velocidad, arma, skin, puntos):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.energia = energia
        self.fuerza = fuerza
        self.defenza = defenza
        self.velocidad = velocidad
        self.arma = arma
        self.skin = skin
        self.puntos = puntos
        print(f"{self.nombre}")
        print(f"{self.nivel}")
        print(f"{self.vida}")
        print(f"{self.energia}")
        print(f"{self.fuerza}")
        print(f"{self.defenza}")
        print(f"{self.velocidad}")
        print(f"{self.arma}")
        print(f"{self.skin}")
        print(f"{self.puntos}")
    def atacar(self):
        print("ATAQUE")
    def defender(self):
        print("DEFENSA")
    def saltar(self):
        print("SALTO")
    def comprar(self):
        print("CACHING")
    def subirNivel(self):
        print("turuturu")

hollow_night = Personaje("The knight", "112%", "9 mácaras de vida", 
    "alma", "21 puntos de daño", None, "caminata constante", 
    "agijón", "caparazon blanco con capa gris", "geo")

hollow_night.atacar()
hollow_night.defender()
hollow_night.saltar()
hollow_night.comprar()
hollow_night.subirNivel()