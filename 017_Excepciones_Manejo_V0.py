#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 017_Excepciones_Manejo_V0 Manejo basico de las excepciones y derivados

try: #la palabra reservada try la utilizamos para probar y buscar errores
    numero_str = input("Ingrese un número entero: ") #Solicitamos al usuario que ingrese un numero
    numero = int(numero_str) #hacemos la conversion entre tipo de variable, de string a int
    
    # Realizamos una operacion con el numero almacenado en la variable tipo int
    resultado = 100 / numero
    print("El resultado de la división es:", resultado) #Imprimimos el resultado de la operacion

except ValueError: #Utilizamos el except para manejar errores en caso de que suceda algun imprevisto al ejecutar el codigo
    #El ValueError nos ayuda a distinguir si se introdujo correctamente un numero y no letras o algun caracter distinto
    print("Por favor, ingrese un número entero válido.") #En caso de que detecte error, se ejecuta la impresion de este mensaje para advertir que hubo un error

except ZeroDivisionError: #Esta excepcion nos ayuda a por ejemplo en la division, que no sea entre 0, ya que normalmente saldria un error de consola, sin embargo aqui nos muestra el mensaje que definimos
    print("No se puede dividir por cero.") #Imprmimos el mensaje en caso de error

except Exception as e: #Esta excepcion nos ayuda a mandar un mensaje en caso de que haya sucedido algun error que no hayamos previsto
    print("Se ha producido un error:", e)

else: #En caso de que no haya errores, se envia un mensaje, para eso sirve el else
    print("La división se realizó con éxito.") #Enviamos un mensaje para informar correcto funcionamiento

finally: #Esta palabra reservada se ejecuta siempre que termina el programa, hayan pasado errores o no 
    print("POR FIN ME PUEDO IR A DORMIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIR") #Imprimimos un mensaje final y nos vamos a dormir por fin, despues de 51 capitulos


