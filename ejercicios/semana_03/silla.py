class Silla:
    def __init__(self,acabado, material, forma, patas, 
        cojin, altura, anchura, grosor, respaldo,
        movilidad):
        self.acabado = acabado
        self.material = material
        self.forma = forma
        self.patas = patas
        self.cojin = cojin
        self.altura = altura
        self.anchura = anchura
        self.grosor = grosor
        self.respaldo = respaldo
        self.movilidad = movilidad
        print(f"{self.acabado}")
        print(f"{self.material}")
        print(f"{self.forma}")
        print(f"{self.patas}")
        print(f"{self.cojin}")
        print(f"{self.altura}")
        print(f"{self.anchura}")
        print(f"{self.grosor}")
        print(f"{self.respaldo}")
        print(f"{self.movilidad}")
    
    def sentarse(self):
        print("te sentaste")
    def mover(self):
        print("la moviste")
    def levantar(self):
        print("levantaste")
    def acomodar(self):
        print("la acomodaste")
    def prestar(self):
        print("te la presto")

silla_gamer = Silla("Mate tecturizado", "Cuero sintético", "baquet", 
    "base de estrella de 5 puntas", "Espuma moldeada", "125cm", 
    "55cm", "10cm", "reclinado a 135 grados", "alta")
        
silla_gamer.sentarse()
silla_gamer.mover()
silla_gamer.levantar()
silla_gamer.acomodar()          
silla_gamer.prestar()        