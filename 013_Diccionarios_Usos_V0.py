#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 13_Diccionarios_Usos_V0 Veremos intorduccion a los diccionarios de python, usos, bucle for, modificar valores,  metodos, etc

#Para comenzar aprenderemos a declarar un nuevo diccionario, es tan sencillo como:
#Consta de claves (key) que son las categorias y valores (value) que son elementos dentro de la categoria
teclado1 = { #Declaramos el nombre del diccionario y abrimos corchete
	'Categoría': 'Teclados', #Podremos tener varias categorias, en las que almacenaremos datos
	'Modelo': 'HyperX Alloy FPS Pro', #Hay que tener en cuenta la sintaxis de cada categoria, dividida entre dos puntos entre nombre y elemento
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados', #No olvidar la coma entre cada cambio de categoria
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
#Para imprimir un dato que necesitemos y se encuentre dentro de una categoria del diccionario:
#Creamos una variable a la que le asignamos el valor del nombre del diccionario y entre parentesis la categoria en que se encuentra el elemento deseado
consulta = teclado1['Modelo']
print(consulta)
#O tambien podemos hacerlo directamente sin guardar el dato en una variable extra, depende del uso que le queramos dar
print(teclado1['Modelo'])
#Para imprimir todo el diccionario completo habra que utilizar el metodo print llamando al diccionario directamente:
print(teclado2)

#Tambien podemos combinar tipos de dato al imprimir un dato de un dicconario
print('El modelo ',teclado2['Modelo'],' cuesta', teclado2['Precio'])

precios={
    'Taco simple' : '$20.00',
    'Orden chica' : '$130.00',
    'Bebida' : '$15.00'
}

#Tambien podemos modificar los datos de un diccionario.
precios['Bebida']='$20.00'
print(precios['Bebida'])

#Podemos ademas usar bucle for para mostrar los datos de un diccionario
#Para esto basta con declarar una variable auxiliar que haga el conteo y busque el dato que se requiere

for x in teclado2: #Se declara el for con la condicional de que x haga el conteo en el diccionario deseado
    print(x, ' = ', teclado2[x], '.') #Se llaman las variables que necesitamos imprimir

#Podemos utilizar el metodo len para contar los elementos de un diccionario
#Podemos tambien utilizar el metodo del para eliminar elementos dentro del diccionario
#Por ejemplo vamos a eliminar el diccionario teclado1 que creamos anteriormente

del teclado1 #Eliminamos completamente el diccionario de nuestro programa

#Tambien podemos elimnar datos especificos de un diccionario:
del teclado2['Categoría']
del teclado2['Precio']#Asi elimnamos dos de las 3 categorias que contiene
#Ahora podemos mostrar todo lo contenido en el diccionario y veremos el cambio:
print('\n',teclado2)

#Ahora podemos combinarlo en un tema nuevo, del ejemplo que yo cree del diccionario tacos, añadiremos una nueva categoria, modificaremos otra y eliminaremos otra
#Para añadir haremos lo siguiente:
precios['Quesadilla']='$25'
precios['Orden']='$120.00'
#Para modificar haremos lo siguiente:
precios['Taco simple']='$18.00'
#Para eliminar usaremos del:
del precios['Orden chica']
#Imprimimos para revisar resultados:
print(precios)
 
