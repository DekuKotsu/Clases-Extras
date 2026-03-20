""" 
Dia 19 de marzo del 2026
Que es una variable de numero entero?
Es un espacio en la memoria donde se guarda numeros complejos, positivos,
negativos y que no tienen punto decimal
Ejemplo
> 5 
> 3i
> -4
-------------------------------------------------------
Operadores aritmetico:
Suma (+)
Resta (-)
Multiplicación (*)
División (/)
Módulo (% o mod): Devuelve el resto de una división entera.
Exponenciación (** o ^): Eleva un número a la potencia de otro.

Ejemplos:

'Suma' (5 + 7)
'Resta' (7 - 4)
'Multiplicacion' (4 * 3)
'division' (2 / 4)
'Modulo' (3 % 7)
'Exponenciales' (5**2)
------------------------------------------------------
"""

variable_uno = int(input("ingresa un numero: "))
variable_dos = int(input("ingresa otro numero: "))
print("------------------------------------------------")
#suma = variable_uno + variable_dos
#print("La suma es:", suma)
#print("------------------------------------------------")
##RESTA
#resta = variable_uno - variable_dos
#print("La resta es:", resta)
#print("------------------------------------------------")
##Multiplicacion
#multiplicacion = variable_uno * variable_dos
#print("La multiplicacion es:", multiplicacion)
#print("------------------------------------------------")
##Division
#division = variable_uno/ variable_dos
#print("La division es:", division)
print("------------------------------------------------")
#modulo
modulo =  variable_uno % variable_dos
print("El modulo de la division de estos 2 numeros es:", modulo)
print("------------------------------------------------")

#Exponentes
exponente = int(input("Ingresa a que potencia deseas ver: "))
exponente_uno = variable_uno **exponente
exponente_dos = variable_dos**exponente
print( variable_uno, "elevada a la:" , exponente, "es:", exponente_uno)
print(variable_dos, "elevada a la:" , exponente, "es:", exponente_dos)
print("------------------------------------------------")
print(exponente_uno-exponente_dos)
""" 
Que es lo que hace el int(input(""))?
lo que es es para el codigo y pedirle al usuario que
ingrese un dato atraves de la terminal y esta se almacen en la 
variabla , como le hayas puesto, como en este caso:
variable_uno,
variable_dos 
y exponente.
El tipo de dato que se guarda es de tipo entero, osea que un numero y no un string, booleano, etc.
El cual esto no puede ser un String es por el "int" que lleva antes del input, y esto nos define 
que lo que se salga va hacer una variable de tipo entero, si se introduce un texto va a marcar error.
"""
