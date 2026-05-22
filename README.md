# Repositorio de Programacion Orientada a Objetos con Python 

# Repositorio con Ejercicios de Programación Orientada a Objetos.
 
##1.Crear .gitignore

Crear el archivo .gitignore para configurar los archivos y carpetas que no deseamos que se guarden en el rrepositorio.

````python
*.pyc
__pycache__/
````

## 2. Indexar archivos y carpetas 

Indexa todos los archivos y carpetas en busca de documentos nuevos.

````python
git add .
````

## 3. Crear un COMMIT

Crea un comit o punto de control de los cambios realizados en el proyecto.

````python
git commit -m "CREATED .gitignore"
````

* CREATED -Se crearon nuevas carpetas
* UPDATED -Se actualizaron o agregaron nuevas funciones
* FIXED - Se corrigieron errores.

## 4. Realizar el COMMIT

Sincroniza los cambios realizados en el repositorio

````python
git push -u origin main
````

## 5. Agregar Documentación a los métodos

agragar un **Docstring** a los métodos generados

**ejemplo**

````python

"""
Este metodo recibe 2 variables enteras, la suma y regresa el resultado de la suma
    
Args:
    
variable_uno:int - Primer numero entero
variable_dos:int - Segundo numero entero
    
:return
    
suma:int - Suma de los dos numeros enteros
    
"""

````

## 0. Deshacer el commit actual
Este comando borra el commit pero mantiene intactos tus archivos y tu código en el área de trabajo:

````python
git reset HEAD~1
````

## 0.1. Crear los 4 commits individuales
Ahora que tus archivos están libres, debes agruparlos y registrarlos uno por uno. 
Repite este proceso para cada uno de tus 4 códigos:
Prepara el primer archivo:

````python
git add ruta/del/archivo1.ext
````

Crea su commit correspondiente:

````python
git commit -m "Agregar primer código"
````
## Si YA habías subido el commit viejo a GitHub
Si el commit agrupado ya aparecía en la página de GitHub, el servidor rechazará tu envío porque estás alterando el historial. 
Para resolverlo, debes obligar a GitHub a aceptar  nuevos commits usando el parámetro --force:

````python
bashgit push -u origin main --force
````
