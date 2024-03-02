#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 015_Clases_Manejo_V0 Clases y objetos, metodos para utilzarlas en general, programacion orientada a objetos

#Para declarar una nueva clase usaremos la palabra reservada class, dentor de la clase podremos delcarar atributos que podemos utilizar en cualquier momento solo llamandolos
#Ademas, podemos definir funciones dentro de las clases, las cuales pueden jugar con los atributos generales

class Perro: #Declaramos una clase llamada perro, utilizando su palabra reservada, nos servira para guardar los datos de tantos perros queramos
#Los atributos de la clase se resumen en guardar el nombre, raza y edad del perro
    def __init__(self, nombre, raza, edad): #Definimos el metodo init que nos ayuda a inicializar los atributos de un objeto basicamente, para tener un estdo inicial y coherente 
        self.nombre= nombre #Como podemos observar, al utilizar init se agrega un atributo llamado self
        self.raza= raza
        self.edad=edad
        

    def imprimir(self): #Declaramos una funcion que nos ayude a imprimir los datos de un perro
        print('Nombre:',self.nombre,'\nRaza: ',self.raza,'\nEdad: ',self.edad,'\n')
#Para definir un objeto a partir de la clase, es decir que cuente con sus atributos, es necesario nombrarlo e igualarlo a la clase, seguido de sus atributos en sus parametros
firu001= Perro('Lily','Pitbull','7 años')
#En caso de que no utilicemos el metodo init, para declarar los atributos de un objeto es necesario hacerlo por separado con otra sintaxis que en lugar de igual sera un punto seguido del atributo a definir
#Podemos definir varios objetos a partir de una misma clase, basta con cambiar el nomobre del objeto y definir sus datos    
firu002= Perro('Arena','Labrador','17 años')

firu001.imprimir() #Ipmprimimos el objeto 1 llamando a la funcion de la clase imprimir
firu002.imprimir()  #Ipmprimimos el objeto 2 llamando a la funcion de la clase imprimir

#Tambien podemos cambiar un solo atributo de un objeto despues de declararlo:
firu002.edad = '16 años' #Se modifica el atributo edad en el objeto dos
#Ademas podemos eliminar atributos de un objeto utilizando la palabra reservada del:
del firu002.raza #Se utiliza la palabra reservada del para eliminar un atributo del objeto 2
#Y podemos definir nuevamente este atributo
firu002.raza = 'Husky' 
firu002.imprimir()  #Ipmprimimos el objeto 2 para comprobar el cambio de atributo y la eliminacion del otro
#Y podemos tambien eliminar el objeto completo, utilizado igual el del pero sin especificar nada mas
#del firu002, esta seria la manera de eliminarlo, no lo dejo funcionando para evitar problemas al correr el codigo completo

#Tambien podemos crear clases vacias, simplemente declarandola y dentro utilizando la palabra reservada pass
#Esto nos puede servir para muchas cosas, yo el uso que le daria es para dejar ciertas banderas o dejar abiertas posibilidades de implementar funciones nuevas en el codigo

class usuarios(): #Declaro una nueva clase que podria abrir posibilidades de extension de codigo
    pass#Utilizo la palabra reservada pass para dejar la clase vacia

#Otro tema por abordar son las herencias, esto se trata de basicamente crear subclases de una superclase que nos ayude a jalar atributos de una a otra, para ahorrarnos varias lineas de codigo y ser menos repetitivo
class PerroPro(Perro): #Defino una subclase que herede los datos de la superclase Perro
    def __init__(self, nombre, raza, edad, cuidado): #Defino los atributos iniciales de la subclase agregando uno extra, tratandose de un cuidado especial para ciertos perros
        super().__init__(nombre, raza, edad) #Llamamos al constructor de la superclase para pasar los datos anteriores y herencia
        self.cuidado = cuidado #Definimos el nuevo atributo de nuestra subclase

    def imprimir(self): #Utilizamos un metodo para imprimir los datos
        super().imprimir() #Se llama al metodo de la superclase encargado de imprimir los datos iniciales, asi ahorramos mas codigo
        print('Cuidado especial:', self.cuidado,'\n')

firup001=PerroPro('Benito','Chihuahua','2 años', 'Frio') #Creamos un nuevo objeto de la subclase, declarando los 3 atributos que se heredan de la superclase y el nuevo atributo de la clase hija
firup001.imprimir()




    
