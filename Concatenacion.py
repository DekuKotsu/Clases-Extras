"""
Dia 18 de Marzo del 2026
Ejemplo de como de hacer un cambio de una variable de tipo entero
a una variable de str (String) y concatenacion 
"""
"""
La concatenacion nos sirve para juntas varios str (String) sin necesidad de poner 
un monton de print ya que esta funcion nos ayuda a unir varios textos dentro de 
un mismo print
"""
Nombre_uno = 'David'
edad = 25
edad_str = str(edad) # estos el 25 convertido a string


print(Nombre_uno + " " + edad_str) #concatenacion 
print(f"{Nombre_uno}, edad {edad} ") 
"""f(sirve para poder agregar varios tipos de datos dentro de un mismo print
por ejemplo strings y datos de numeros enteros, pero los numeros enteros van dentro de 
llaves para que se pueda ejecutar ({}) y no marquen un error"""

Nombre = "Ivan Adriel"
Edad = 19 
Altura = 1.70

edad_str=str(Edad)
altura_str=str(Altura)
print (altura_str)
print(Altura)
print("Nombre:" + Nombre + "\n"+ "Edad:" + edad_str +  "\n" + "Altura:" + altura_str +"m" )
print(f"Mi nombre es {Nombre}, mi edad es {Edad} y mi estatura es {Altura:.2f}m")
