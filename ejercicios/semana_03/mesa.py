class Mesa:
    def __init__(self, acabado, material, forma, patas, 
        tablero, altura, anchura, grosor, almacenamiento_integrado, 
        movilidad ):
        self.acabado = acabado
        self.material = material
        self.forma = forma
        self.patas = patas
        self.tablero = tablero
        self.altura = altura
        self.anchura = anchura
        self.grosor = grosor
        self.almacenamiento_integrado = almacenamiento_integrado
        self.movilidad = movilidad
        print(f"{self.acabado}")
        print(f"{self.material}")
        print(f"{self.forma}")
        print(f"{self.patas}")
        print(f"{self.tablero}")
        print(f"{self.altura}")
        print(f"{self.anchura}")
        print(f"{self.grosor}")
        print(f"{self.almacenamiento_integrado}")
        print(f"{self.movilidad}")
    def sentarse(self):
        print("Bajate de ahi")
    def limpiarlo(self):
        print("pish pish")
    def ensuciarlo(self):
        print("ASCOOO")
    def rayarlo(self):
        print("NO HAGAS ESOOOO")
    def acomodar(self):
        print("acomodaste cosas")
    
mesa_redonda = Mesa("Barniz poliuretano transparente", 
    "Madera de roble", "Circular", "1 Pedestal central unico", 
    "Plano", "75cm", "110cm", "3cm", "Ninguno", "Estatica")

mesa_redonda.sentarse()
mesa_redonda.limpiarlo()
mesa_redonda.ensuciarlo()
mesa_redonda.rayarlo()
mesa_redonda.acomodar()