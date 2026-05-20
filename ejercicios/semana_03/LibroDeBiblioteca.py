class LibroDeBiblioteca:
    def __init__(self, numero_de_paginas, numero_de_id, autor, 
        genero, editorial, idioma, anio_de_edicion, pasta, material, 
        numero_de_tomo):
        self.numero_de_paginas = numero_de_paginas
        self.numero_de_id = numero_de_id
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.idioma = idioma
        self.anio_de_edicion = anio_de_edicion
        self.pasta = pasta
        self.material = material
        self.numero_de_tomo = numero_de_tomo
        print(f"{self.numero_de_paginas}")
        print(f"{self.numero_de_id}")
        print(f"{self.autor}")
        print(f"{self.genero}")
        print(f"{self.editorial}")
        print(f"{self.idioma}")
        print(f"{self.anio_de_edicion}")
        print(f"{self.pasta}")
        print(f"{self.material}")
        print(f"{self.numero_de_tomo}")
    
    def entretener(self):
        print("WOOOOW")
    def leer(self):
        print("leer el libro")
    def educar(self):
        print("Comprende el libro")
    def cuidar(self):
        print("Cuida el libro")
    def imaginar(self):
        print("Imagina")

imaginaria = LibroDeBiblioteca("96", "9798846335974", "kristopher Rodas", 
    "literatura y ficcion", "Nass papier", "Español", "2022", 
    "Pasta blanda", "Cartulina y papel bond", "Libro 1")

imaginaria.entretener()
imaginaria.leer()
imaginaria.imaginar()
imaginaria.educar()
imaginaria.cuidar()
    