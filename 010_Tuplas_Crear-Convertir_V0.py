#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 10_Tuplas_Crear-Convertir El tema general de esta practica seran las tuplas, desde crearlas hasta convertirlas a listas y visceversa

#Para comenzar crearemos una tupla de colores y la imprimiremos, a diferencia de las listas, las tuplas se declaran con parentesis:

colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')

#Para imprimir una tupla se utiliza la misma metodologia que con las listas, ademas podemos imprimir los valores con sus direcciones, tanto positivos como negativos

print("\n\nEl elemento de la segunda posicion de la tupla 'colores' es: ", colores[1])

#Tambien podemos realizar operaciones con los elementos de una tupla, en este caso creamos una tupla con 4 digitos y queremos utilizar sumas y restas para obtener un valor de 25 y almacenarlo en una variable nueva:

numeros = (10, 1, 5, 11)
#Creamos la variable operacion para dentro de ella llamar los valores de la tupla necesarios para obtener el resultado deseado
operacion= numeros[0]+numeros[3]+numeros[2]-numeros[1]
#Imprimimos la variable con el resultado:
print(operacion)
#Como pudimos observar el uso de tuplas es sencillo al igual que las listas

#Otra manera de trabajar las tuplas es convertirlas a listas para poder variar sus elementos y visceversa
#Para convertir una lista en una tupla debemos utilizar el metodo tuple como veremos a continuacion, primero creamos una lista

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#Para hacer el cambio generamos una nueva variable donde quedaran guardados los datos y actuamos con el metodo list
listacol=list(colores)
print(listacol)
print(type(listacol)) #El metodo type nos ayuda a saber el tipo de de dato que es algo en python
#Pudimos observar el correcto funcionamiento, ahora haremos un cambio a la lista nueva y despues la pasaremos a una tupla:
listacol.remove('rojo') #Eliminamos el primer dato de nuestra lista
tuplacol=tuple(listacol) #Utilizamos el metodo tuple para cambiar de lista a tupla
print(tuplacol) #Imprimimos la tupla observando el cambio
print(type(tuplacol)) #Verificamos el tipo de dato

