#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 9_Listas_Insertar-Acomodo En esta version de practica referente a listas observaremos el comportamiento de los metodos usados para insertar, ordenar y contar elementos

#Comenzamos creando nuestra lista base:
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Primero veremos el metodo append, nos sirve para añadir elementos a la lista despues de la ultima posicion. 
#A esta lista añadiremos los colores 'fuxia' y 'celeste' de la siguiente manera:
#El .append es muy sencillo, colamente en el parametro agregamos el elemento que queremos insertar y listo
colores.append("fuxia")
colores.append("celeste")

#Imprimimos la lista con los nuevos elementos y podemos observar que funciona correctamente
print(colores)

#Ahora utilizaremos el metodo insert(), a diferencia del anterior, este maneja dos parametros, el primero indica la posicion en donde queremos insertar el elemento nuevo y en el segundo parametro colocamos el elemento deseado

#A la lista anterior queremos agregar  los colores 'magenta' y 'turquesa', a magenta lo colocaremos en la posicion siguiente a la de lila, y turquesa en la penultima posicion, queda de la siguiente manera:
colores.insert(6,"magenta")
colores.insert(-1,'turquesa')
#Imprimimos la actualizacion de nuestra lista y podemos observar que los elementos se integraron perfectamente acorde lo necesitado
print(colores)

#Pasemos a ordenar elementos, en este caso utilizaremos los metodos sort y sorted.
#El metodo sort() ordenara alfabeticamente la lista en orden ascendente, en caso de necesitarlo descendente debemos ingresar un reverse=True dentro del parametro de sort, solamente tener en cuenta que los cambios de sort son permanentes, si queremos mostrar el acomodo de manera temporal se utilizara el metodo sorted
#Haremos un ejercicio que ordenara la lista deseada en orden alfabético descendente 
#Creamos la lista:

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco','naranja']
#Incluimos los dos metodos y mostramos el orden alfabetico tanto descendente como ascendente, uno con cada uno
colores.sort(reverse=True)
#Imprimimos los metodos y observamos el correcto funcionamiento
print(sorted(colores))
print(colores)


#Por ultimo veremos el metodo len(), que es utilizado para contar los elementos dentro de una lista y puede ser almacenado en una variable, vamos a utilizarlo para contar la ultima lista y mostrar una variable que indique este numero:
longitud=len(colores)
#se imprime la cantidad de elementos que tiene la lista
print("\nLa lista colores tiene un total de ",longitud," elementos")




