#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 3_Concatenar Concatenar strings en diferentes variables

#Declaramos y concatenamos dos strings en una sola variable y mostramos el resultado
prueba="Por ti, "+"haria lo que fuera por ti"
print(prueba) #Imprimimos para ver el resultado

#Declaro en 3 variables mi nombre, dos individuales y una con mis dos apellidos
n1="ALDO " #Se declara el nombre con un espacio
n2="EMILIANO " #Segundo nombre con un espacio
n3="CHAVEZ LARES"
#Declaro mi registro en dos variables para concatenar y mostrar
r1='2131'
r2='0238'
com=n1+n2+n3 #Se suman los strings para mostrar el nombre completo
reg=r1+r2 #Se suman los strings para mostrar el registro, al estar en comilla no se suman los digitos
#Se muestra la concatencion completa
print(com,reg)

#Jugamos con el concepto para terminar de comprender
v1="Oye mami llevame a un lugar mejor" #Declaramos una linea de texto
v2="\nDonde no haya oscuridad solo haya sol" #Declaramos otra linea de texto
v3="\nSe que puedes hacerlo porque tienes el don"
can=v1+v2+"\nDonde no haga frio, solo haga calor"+v3 #Unimos lineas de texto para ver funcinamientos
print(can)#Imprimimos y vemos resultados
