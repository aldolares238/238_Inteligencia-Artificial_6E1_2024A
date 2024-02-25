#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 10_Tuplas_Comprobar-Datos En esta segunda parte de la practica vamos a aprender a comprobar si un dato esta dentro de una tupla o lista

#Para este ejercicio crearemos una tupla con 4 colores
colores=('rojo','azul','verde','negro')
#Solicitamos al usuario que ingrese un color que cotejaremos con la tupla creada
dato=input('Introduzca un color:\n')
#Declaramos una serie de condicionales para comprobar si el color ingresado por el usuario se encuentra dentro de la tupla creada

if  dato in colores[0]:     #Utilizamos la palabra reservada 'in' para cotejar una variable dentro de una tupla o lista, esto nos ayuda a saber si se encuentra dentro de ella
        print('El color rojo si se encuentra guardado')
elif dato in colores[1]:
    print('El color azul si se encuentra guardado')
elif dato in colores[2]:
    print('El color verde si se encuentra guardado')
elif dato in colores[3]:
    print('El color negro si se encuentra guardado')
else:
    print('El color ',dato,' NO esta en el parametro')
