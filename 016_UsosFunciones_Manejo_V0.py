#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 016_UsosFunciones_Manejo_V0 Uso de variables globales, locales, funcones anidadas, modulos, lambda, expresiones regulares, metacaracteres



#Declaramos variables globales en nuestro programa, para que en cualquier punto se puedan usar y llamar
proyecto_actual = "Programacion PLC213"
horas_trabajadas = 0

def registrar_horas(horas): #Definimos una primer funcion que nos ayude a registrar las horas de trabajo enpleadas
    global horas_trabajadas #Llamamos a la variable global de horas trabajadas

    def calcular_costo(): #Definimos una segunda funcion dentro de la primera, esto ocasiona que queden anidadas
        costo_por_hora = 300  #Definimos una variable local de nuestra segunda funcion que nos permita dar un valor a las horas de trabajo
        costo_total = horas * costo_por_hora #En una nueva variable operamos el costo por hora de la variable local multiplicado por las horas trabajadas del atributo
        return costo_total #Regresamos el valor final

    costo_horas = calcular_costo()  #Llamamos a la funcion anidada interna para calcular el costo
    horas_trabajadas += horas  # Actualizamos el total de horas trabajadas
    print(f'Se registraron {horas} horas de trabajo en el proyecto "{proyecto_actual}".') #Imprimimos la cantidad de horas registradas en el proyecto
    print(f'Costo total por estas horas: ${costo_horas}.') #Imprimimos el costo de esas nuevas horas trabajadas
    print(f'Total de horas trabajadas en el proyecto: {horas_trabajadas} horas.') #Imprimimos la actualizacion de las horas totales empleadas en el proyecto

# Probamos la función
registrar_horas(10) #Llamamos a la funcion principal y le damos el atributo de 10 horas
registrar_horas(15) ##Llamamos a la funcion principal y le damos el atributo de 15 horas y comprobamos el funcionamiento

#Por otro lado tenemos el uso de los modulos, que son basicamente bibliotecas que podremos importar con la palabra reservada import
import math #Importamos a nuestro programa la biblioteca llamada math, para utilizar funciones matematicas de todo tipo
import datetime #Importamos un modulo que nos ayuda a mostrar fechas actuales
import re #Importamos el modulo re que nos aporta las expresiones regulares, secuencias de caracteres que forman un patron de busqueda
#Tambien tendremos el uso de lambda, que basicamente se utiliza para definir funciones anonimas o pequeñas de una sola linea, sirven al hacer funciones rapidas de tareas simples

area_circulo = lambda radio: (math.pi*radio**2) #Definimos nuestra funcion anonima para calcular el area de un circulo, utilizando lambda para hacerlo en una sola linea
#Ademas utilizamos el math.pi, elemento que nos da el valor concreto de pi extraido de la biblioteca math anteriormente importada
print('\nEl area del circulo con radio 15 utilizando lambda en la funcion es: \n',area_circulo(15)) #Llamamos a la funcion anonima definiendo su parametro de radio e imprimimos
fecha = datetime.datetime.now() #Declaramos una nueva variable a la que le asignamos la fecha actual para ser mostrada, extraida del modulo datetime anteriormente importado
print('\nEste codigo tan interesante esta siendo corrido en la fecha:\n',fecha) #Imprimimos la fecha actual de la variable creada
#Tenemos un concepto nuevo, el strftime(), es una funcion que nos sirve a darle bastantes tipos de formato a las fechas
print(fecha.strftime('\nEl dia de la semana actual es: %A, del mes %B, del año %G',)) #Uso del strftime() para mostrar el dia actual, mes y año

rola= 'Lo que no fue no sera' #Declaramos una variable que contenga una linea de texto cualqueira
busca = re.search('que', rola)#Utilizamos la funcion search del modulo re anteriormente importado, buscando la linea de caracteres 'que', qe nos mostrara como resultado la posicion en donde se encuentra
#La funcion search del modulo re solamente busca hasta el primer elemento que coincida, los demas los descarta
print(busca)#Observamos lo que encontro, vemos que nos muestra la direccion de los caracteres
#Sin embargo tenemos otra funcion  que busca todos los elementos aunque esten repetidos, el findall
frase= 'La vida es un chiste, ja ja ja, ven cuentamelo' #Declaramos una frase que contenga 3 veces una linea de dos caracteres para buscar
busca= re.findall('ja', frase)#Buscamos todas las veces que se repita 'ja' dentro de la frase con a funcion findall
print(busca)#Observamos lo que encontro, nos regresa las 3 veces que se encuentra esa linea

cancion = 'Me tienes mirándome al espejo, Yo que nunca tuve ni un complejo, Tú eres como Ariana, mi primer amor, Y yo estoy como Miller, en la depresión, Ahora te ando buscando, pensando, escribiendo, Y tú toda empoderada, ¿qué andarás haciendo?'
busca= re.split('e',cancion) #Usamos la funcion split para dividir el texto y excluir todo lo que le declaremos, ademas de separarlo
print(busca)#Observamos el comportamiento, cada que encuentra una e, corta el texto y se pasa a la siguiente linea de caracteres
busca= re.split('e', cancion, 5) # usamos el maxplit, El maxsplit se trata de una funcion que limita el numero de coincidencias que devuelve el split, y lo declaramos como el tercer parametro de la funcion split
print(busca) #Observamos que despues de la quinta devolucion, el texto se mantiene tal cual sigue
busca= re.sub(' ', ' YA QUIERO TERMINAR ', cancion) # Tambien tenemos la funcion sub, que basicamente reemplaza lo  que declaremos en el primer parametro por lo que pongamos en el segundo, de una linea de texto
print(busca) #Imprimimos y observamos que en cada espacio de la linea de texto se reemplaza por la frase propuesta
busca = re.sub(' ', ' YA TENGO HAMBRE',cancion, 5)#Tambien podemos limitar el numero de veces que se reemplaza con el sub, esto lo hace la funcion coun, representada en el tercer argumento de la funcion
print(busca) #Observamos que los primeros 5 espacios se reemplazan por la frasae propuesta y lo demas continua tal cual
busca = re.findall('[a-f]',cancion) #Uso de los metacaracteres en findall, nos permite buscar los caracteres entre a la y la f en la linea de texto
print(busca) #imprimimos los caracteres encontrados

#En las siguientes lineas de codigo se implementaran varios casos de metacaracteres para buscar coincidencias en el texto
busca= re.findall('ni un com',cancion) #Buscamos coincidencias dentro del texto y lo implementamos en un if para saber si las hay o no
if busca:
    print('Hay al menos una coincidencia')
else:
    print('No hay coincidencias')

busca= re.findall('complejo | ni un',cancion) #Buscamos coincidencias usando la barra vertical para separarlas dentro del texto y lo implementamos en un if para saber si las hay o no
if busca:
    print('Hay al menos una coincidencia')
else:
    print('No hay coincidencias')

busca= re.findall('^Me',cancion) #Buscamos coincidencias al inicio de la cadena con ^ 
if busca:
    print('Hay al menos una coincidencia')
else:
    print('No hay coincidencias')
    





