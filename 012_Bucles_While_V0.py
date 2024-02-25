#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 012_Bucles_While Uso del bucle while, implementacion y analisis, ademas combinar while con condicional if, so de continue y break

#Para el primer ejercicio crearemos un bucle while que se ejecute hasta que x valga 15, incrementando el valor de dicha variable de 5 en 5
#Para comenzar creamos nuestra variable inicial x
x=0
#Iniciamos el ciclo while y declaramos la condicion para que se mantenga mientras x sea menor o igual a 15
while x<=15:
    print(x)
    x+=5
#Otro ejercicio seria el crear un bucle que se ejecute hasta que x valga -100, con decrementos de 20
#Primero creamos nuestra variable inicialmente en 0
x=0
#Para el while declaramos la condicion que x sea mayor o igual a -100 y decrementamos su valr
while x>=-100:
    print(x)
    x-=20
#Para un tercer ejercicio, haremos que el bucle se ejecute hasta que x valga 0, con decrementos de 1 y mostrar un mensaje con el valor
#Declaramos la variable
x=10
while x>=0:
    print("El valor de x es igual a ",x)
    x-=1

#Tambien podemos jugar con los metodos continue, break e implementar if dentro del bucle while para crear distintas acciones:
#Declaramos x
x=0
#Iniciamos el bucle con la condicion de que x sea menor que 30
while x<=30:
    x+=1 #Incrementamos en una unidad el valor de x
    #Declaramos la primer condicional if para hacer los saltos de ejecucion del bucle
    if x==4 or x==6 or x==10:
        print('Se salto el valor ',x,' de x')
        continue
    #La segunda condicional para este programa se encargara de terminar el bucle
    if x==15:
        print('Se rompio la ejecucion del bucle cuando x valia ',x)
        break
    print(x) #Imprimimos la variable para ver el cambio en tiempo real

#Si queremos jugar con el concepto podemos combinarlo con una lista

lista=['Mañana','sera','otro','dia'] #Declaramos una lista con varios conceptos
x=0 #Inicializamos en 0 una variable para conteo
while x<=10: #Declaramos la condicion, la hacemos en 10 para utilizar el break despues
    print(lista[x])
    x+=1
    if x==len(lista):
        print('Ya no hay mas elementos en la lista')
        break
    

    
       


    
