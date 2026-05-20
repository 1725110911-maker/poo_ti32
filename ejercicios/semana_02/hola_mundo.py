class NombreClase:

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Metodo Uno")

    def metodoDos(self, variable_uno:int, variable_dos:float) ->int:
        """
        Este metodo recibe 2 variables enteras, la suma y regresa el resultado de la suma
    
        Args:
    
        variable_uno:int - Primer numero entero
        variable_dos:int - Segundo numero entero
    
        :return
    
        suma:int - Suma de los dos numeros enteros
    
        """
    
    def metodoTres(self, variable_tres:str)->None:
        print(f"Número de caracteres: {len(variable_tres)}")

nombre_objeto = NombreClase ()
nombre_objeto.metodoUno()
nombre_objeto.metodoDos(10, 15.5)
nombre_objeto.metodoTres("Hola")