#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 014_Funciones_Manejo_V0 Crear y llamar funciones, asi como uso de parametros, entre otras cosas

#Para crear una funcion nueva debemos utilizar la palabra reservada def
def suma(num1, num2): #Al final del nombre de dicha funcion debemos añadir parentesis, estos pueden ir libres o con parametros que la funcion necesite, seguidos de dos puntos
    print(num1+num2)

suma(15,15) #Podemos mandar llamar a la funcion tantas veces queramos, y podemos ingresarlos parametros que necesitamos al momento de llamarla
suma(45,5) #Ademas, cada que llamemmos a la funcion, se ejecutara por separado entre cada llamado, por lo que podemos ahorrar codigo en funciones repetitivas
suma(56999,1)

#Por ejemplo podemos combinar funciones para ahorrarnos codigo
def area(radio): #Definimos una funcion que calcule el area de un circulo y usamos como parametro externo la variable del radio
    return 3.1416*radio**2 #Utilizamos un return para que la funcion nos regrese el dato ya operado
def vol(radio): #Usamos otra funcion que calcule el volumen de una esfera, pero con el mismo parametro de radio de la funcion anterior
    return (4/3)*3.1416*radio**3 #Regresamos el valor operado

radio=float(input('Ingrese el radio de la esfera')) #Hacemos que el usuario deba introducir el valor del radio, y ese valor lo convertimos a flotante para poder trabajar con el
a1=area(radio) #Almacenamos el resultado de area en una variable llamando a la funcion de area
v1=vol(radio) #Almacenamos el resultado de area en una variable llamando a la funcion de volumen
print('El area del circulo es: ',a1,'\n\nEl volumen de la esfera es: ',v1) #Imprimimos ambos resultados

#Tambien vamos a conocer los *args y **kwarks, que basicamente son dos tipos de dato a ingresar en la funcion, el arg es para valores generales y el kwarg para diccionarios

def tacos(*carnes,**bebida): #Definimos una nueva funcion con parametro tipo *args y **kwargs, donde almacenaremos la cantidad de valores que queramos
    print('Hay tacos de:\n') #Imprimimos un primer mensaje para separar a los valores tipo arg
    for arg in carnes: #Para imprimir todos los valores que se definan lo usamos con un for 
        print(arg) #Imprmimimos todos los valores tipo arg

    print('\nY bebidas de:\n') #Separamos a los kwargs con un segundo mensaje 
    for clave, valor in bebida.items(): #Para imprimir todos los valores tipo kwarg, buscamos dos variables en un for, ya que hablamos de un diccionario
        print(f'{clave}: {valor}') #Utilizamos la 'f' antes de la cadena para imprimir una cadena de formato, que nos ayudara a imprimir el diccionario de datos de manera correcta

tacos('Pastor', 'Chorizo', 'Suadero', leche='Horchata', agua='Jamaica') #Mandamos a llamar la funcion general y le declaramos los datos tipo kwarg y arg separados por comas



