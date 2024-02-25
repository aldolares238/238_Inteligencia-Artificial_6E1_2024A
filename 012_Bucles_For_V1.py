#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 012_Bucles_For Implementacion y analisis del bucle for, ademas de uso del metodo range() y pass

#Vamos a crear un bucle for que itere una tupla y muestre una frase con los datos
#Creamos nuestra tupla y declaramos los elementos:
colores = ('rojo','azul','verde','amarillo')
for x in colores: #La condicion iterara cada elemento dentro de nuestra tupla
    print('El color es: ',x,'.') #Imprimimos la frase acompañada del elemento de la tupla en la posicion x

#Por otro lado tenemos el metodo range(), este nos ayuda a acompañar al for
#El metodo puede tener desde 1 hasta 3 parametros, al tener 3, el primero indicara el inicio del ciclo, el segundo indicara el final, y el tercer el decremento o incremento
#Haremos un buble que vaya desde el 7 hasta el 700 con incrementos de 100 en 100
for x in range(7,708,100): #Hay que tomar en cuenta que si queremos que termine en uun numero, el segundo parametro le deberemos sumar una unidad, es decir, si necesitamos que finalice en 7, deberemos colocar un 8 en el parametro
    print(x)

#Podemos tambien combinarlos con elementos de una lista y hacer operaciones con ellos:
#Declaramos la lista:
lista=[1, 2, 3, 4, 5]
x=2 #El valor por el que vamos a multiplicar los elementos
for y in range(len(lista)): #La condicion indica que llame a la longitud de la lista
    res=lista[y]*x #Guardamos en una nueva variable el valor de la operacion
    print(res) #Imprimimos el resultado

