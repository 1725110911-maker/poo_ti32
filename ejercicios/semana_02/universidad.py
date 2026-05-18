class Universidad:
    def __init__ (self, logo, oferta_educativa, localidad,
        si, modalidad, servicios, ubicacion, talleres,
        cantidad_de_salores, rector):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.si = si
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres
        self.cantidad_de_salones = cantidad_de_salores
        self.rector = rector
        print(f"logo:{self.logo}")
        print(f"Oferta educativa:{self.oferta_educativa}")
        print(f"Localidad:{self.localidad}")
        print(f"Sistema informatica:{self.si}")
        print(f"Modalidad:{self.modalidad}")
        print(f"Servicios:{self.servicios}")
        print(f"Ubicacion:{self.ubicacion}")
        print(f"Talleres:{self.talleres}")
        print(f"Cantidad de salores:{self.cantidad_de_salones}")
        print(f"Rector:{self.rector}")

unideh = Universidad("logo.jpg", "ing.software, turismo alternativo", 
    "San miguel", "CADU", "Virtual", "Biblioteca digital", 
    "santa catarina", None, None, "Octavio Castillo")
