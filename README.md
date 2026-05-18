# Repositorio de Programacion Orientada a Objetos con Python 

# Repositorio con Ejercicios de Programación Orientada a Objetos.
 
##1.Crear .gitignore

Crear el archivo .gitignore para configurar los archivos y carpetas que no deseamos que se guarden en el rrepositorio.

````shell
*.pyc
__pycache__/
````

## 2. Indexar archivos y carpetas 

Indexa todos los archivos y carpetas en busca de documentos nuevos.

````shell
git add .
````

## 3. Crear un COMMIT

Crea un comit o punto de control de los cambios realizados en el proyecto.

````shell
git commit -m "CREATED .gitignore"
````

* CREATED -Se crearon nuevas carpetas
* UPDATED -Se actualizaron o agregaron nuevas funciones
* FIXED - Se corrigieron errores.

## 4. Realizar el COMMIT

Sincroniza los cambios realizados en el repositorio

````shell
git push -u origin main
````

## 0. Deshacer el commit actual
Este comando borra el commit pero mantiene intactos tus archivos y tu código en el área de trabajo:
````shell
git reset HEAD~1
````

## 0.1. Crear los 4 commits individuales
Ahora que tus archivos están libres, debes agruparlos y registrarlos uno por uno. 
Repite este proceso para cada uno de tus 4 códigos:
Prepara el primer archivo:
````shell
git add ruta/del/archivo1.ext
````

Crea su commit correspondiente:
````shell
git commit -m "Agregar primer código"
````
