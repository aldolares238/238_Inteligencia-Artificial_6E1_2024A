#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 11_Condicionales En esta practica veremos el uso del condicional IF, operadores de comparacion y el condicional if else, entre otros

#En el primer ejercicio tendremos dos datos numericos, y necesitamos hacer que la condicion del if sea verdadera:

num1 = 15
num2 = 20
#El condicional if consta de comparaciones entre elementos para realizar determinada accion, si la condicion o condiciones se cumplen, se hara la accion que se engloba al if, en caso contrario no hara nada
if num1 < num2:
	print('15 es menor que 20') #Es importante recordar que la accion englobada al if debera ser acompañada de una tabulacion para que el programa lo reconozca correctamente

#Otro ejemplo para este condicional:

num1 = 1450
num2 = 60

if num1 > num2:
	print('1450 es mayor que 60')
#Se cumple la condicion por lo que se ejecuta la instruccion
#Otro ejemplo puede ser cuando no se cumple la condicion:

num1 = 1450
num2 = 60

if num1 == num2:
	print('No se va a ejecutar')

#Como podemos observar al no cumplirse la condicion no se ejecuta la instruccion siguiente

#Otra condicional que podemos manejar es el IF ELSE:
#Este condicional es basicamente una alternativa a la instruccion del if principal, y nos da la opcion de que ocurra otra cosa en caso de que no se cumpla la condicion, no que simplemente no haga nada

color = 'rojo' #Declaramos una variable nueva
if color != 'rojo': #Importante colocar dos puntos seguido de la condicion
	print ("El color no es rojo.") #Recordar el uso de tabulacion en la instruccion
else: #Para declarar el else es necesario simplemente ponerlo al mismo nivel que el if inicial y no lleva condicion adicional
	print ("El color es rojo.")

#Como pudimos observar se cumple la condicion y se ejectuta la primer instruccion, sin embargo, en el siguiente ejemplo veremos un caso en que no se cumple:

num=10
if num<8:
	print("10 es menor que 9")
else:
	print("10 es mayor que 8")


#La siguiente parte de esta practica contiene uso de las condiciones elif, que nos ayudan a poner mas de dos condiciones en caso de ser necesario, no solo verdadero y falso, ademas veremos el uso del metodo input(), este ultimo nos da la opcion de que el usuario ingrese datos al programa
#El ejercicio siguiente muestra una variable en que el usuario ingresara su edad, una vez hecho esto, se cotejara el resultado con varios condicionales para imprimir un mensaje acorde al numero introducido:

edad = int(input('¿Cuál es tu edad?\n')) #El metodo input() hace posible que el usuario ingrese datos

if edad <= 0:	#Declaramos nuestro primer condicional if
	print('Nadie puede tener esa edad.') #No olvidemos la tabulacion
elif edad <= 18:	#Iniciamos con el uso del condicional elif, lo cual nos da la opcion de añadir otra posible condicion para el valor inicial agregado
	print('Eres menor de edad.')
elif edad <= 45:
	print('Eres mayor de edad.')
elif edad <= 100 and edad < 100:
	print('Ya estas viejo')
elif edad <=120:
	print('Ya te reclama la tierra')
elif edad > 120:
	print('¿Como sigues aqui?')
else:	#Si ya no queda otra opcion o condicion, ahora si podemos escribir el 'else', ayudandonos a que si no se cumplio ninguna de nuestras condiciones anteriores, se ejecute cierta instruccion
	print('Edad no válida.')

#Otra manera de tener mas condiciones es encadenando multiples if sin la necesidad de ningun ese o elif:

dato = (input('Introduce una letra de la palabra "love":\n'))

if dato == 'l':
    print('Is for the way you look at me')
if dato == 'o':
    print('Is for the only one I see')
if dato == 'v':
    print('Is very very, extraordinary')
if dato == 'e':
    print('Is even more than anyone that you adore can')

