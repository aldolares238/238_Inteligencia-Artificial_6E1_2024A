#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 9_Listas-Eliminar Lo primero a hacer en esta practica es Utilizar posiciones negativas para imprimir elementos de una lista. 

#Primero declaramos la lista como lo pide el ejercicio:
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Se nos pide mostrar los colores 'naranja', 'amarillo', 'lila', 'blanco' y 'rojo', yo lo haré directamente con una sola instrucción de print() accediendo con sus posiciones negativas y mostrandolas a manera de lista
print("\n\nEn la ultima posicion tenemos el color: ", colores[-1],"\nEn la cuarta posicion tenemos el color: ", colores[-7], "\nEn la sexta posicion tenemos el color: ", colores[-5], "\nEn la penultima posicion tenemos el color: ", colores[-2], "\nEn la primer posicion tenemos el color: ", colores[-10])

#Podemos tambien combinar posiciones negativas y positivas dentro de una lista, y mostrarlas en conjunto con strings
#Creamos una lista cualquiera, en este caso se usaran sabores de paleta
sabor=["vainilla","chocolate","fresa","nuez","oreo"]
msj="\n\nBienvenido a la mejor paleteria"
#En este ejemplo se uso un conjunto de conceptos anteriormente aprendidos durante el curso, combinando el uso de strings, listas, saltos de linea, etc
print(msj,"\n\tTenemos varios sabores como:","\n\t",sabor[1],"\n\t",sabor[2],"\n\t",sabor[-1],"\n\t",sabor[-2],"\n\t",sabor[0])

#Por otro lado, tambien veremos el como eliminar elementos con distintos metodos, ya sean del(), remove(), pop(), append()
#Primero creamos la lista deseada:

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Ahora vamos a eliminar los colores 'azul', 'marrón', 'negro' y 'rosa', utilizando el metodo del(), para hacerlo simplemente debemos escribir el metodo acompañado del nombre de la lista, y dentro de su parametro introducir la direccion del elemento que necesitamos eliminar:
#Es importante mencionar que al eliminar un elemento, se actualizan las direcciones de la los demas elementos dentro de la lista, por lo que despues de eliminar algo, otro valor toma su posicion a manera de corrimiento, ademas recordar que podemos utilizar posiciones negativas
del colores[1]
del colores[3]
del colores[4]
del colores[-3]

#Una vez eliminados los elementos deseados, mostramos la lista con un print
print(colores)

#Pudimos observar bien el comportamiento del metodo del
#Ahora probaremos eliminar elementos con otro metodo, esta vez con remove(), la sintaxis es un poco diferente, debera ser el nombre de la clase seguido de un .remove, y entre parentesis el elemento textual que queremos eliminar, no su posicion
#Siguiendo con la lista anterior, eliminaremos los  elementos 'amarillo' y 'rojo'

colores.remove("amarillo")
colores.remove('rojo')

#Procedemos a imprimir la clase para ver el resultado

print(colores)

#Se observa el comportamiento del remove

#Siguiendo con los metodos de eliminacion tenemos el pop(), en este caso, tambien se introduce la posicion en la lista de lo que queremos eliminar, sin embargo tiene el plus de que lo podemos almacenar en otra variable y tener el dato guardado aunque ya no exista en la lista
#Para hacer el ejemplo tenemos la siguiente lista de colores que volvemos a declarar:

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Se desea eliminar los elementos 'azul' y 'blanco', ademas los vamos a guardar en una nueva lista, quedara de la siguiente manera:

col=[colores.pop(1),colores.pop(7)] #En esta sola linea creamos una nueva lista con los elementos eliminados de la anterior, haciendo uso del metodo pop y recordando de recorrer la posicion del segundo elemento ya que previamente eliminamos otro
#Procedemos a imprimir la lista con los elementos eliminados, podemos observar que ya no aparecen los datos 'azul' y 'blanco'
print(colores)
#Ahora imprimimos nuestra nueva lista con los dos elementos que quitamos previamente con el metodo pop:
print(col)
