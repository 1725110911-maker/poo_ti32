class Alumno:
    def __init__(self, nombre, matricula, edad, carrera, cuatrimestre, 
        promedio, correo, materias, direccion, becas):
        
        self.nombre = nombre
        self.matricula = matricula
        self.edad = edad
        self.carrera = carrera
        self.cuatrimestre = cuatrimestre
        self.promedio = promedio
        self.correo = correo
        self.materias = materias
        self.direccion = direccion
        self.becas = becas
        print(f"{self.matricula}")
        print(f"{self.nombre}")
        print(f"{self.edad}")
        print(f"{self.carrera}")
        print(f"{self.cuatrimestre}")
        print(f"{self.promedio}")
        print(f"{self.cuatrimestre}")
        print(f"{self.materias}")
        print(f"{self.direccion}")
        print(f"{self.becas}")

    def inscribirce(self):
        print("QUE HICISTE")
    def estudiar(self):
        print("MENTIROSO")
    def entregarTareas(self):
        print("APOCO SI LO HICISTE TU")
    def calificaciones(self):
        print("Pansaste")
    def colejiatura(self):
        print("Mantenla")

luis = Alumno("Luis Alberto Gómez Ramírez", "2024031409", "20 años", 
    "Ingeniería en Software", "Quinto cuatrimestre", "9.4", 
    "luis.gomez@universidadficticia.edu.mx", "Estructuras de Datos, Base de Datos Avanzadas, Desarrollo Web Orientado a Servicios, Programación Móvil y Probabilidad y Estadística", 
    "Calle Los Pinos #405, Colonia Centro, C.P. 42000, Pachuca, Hidalgo", "Beca de Excelencia Académica")

luis.inscribirce()
luis.estudiar()
luis.entregarTareas()
luis.calificaciones()
luis.colejiatura()
