"""
Que es el if?
El if es un control de flujo que nos permite ejecutar un bloque de codigo, 
solo si cumple una condicion espcifica 

Para que nos sirve?
Nos sirve para hacer una toma desiciones 
Ejemplo:
x >= 0 

Como se estructura?
Al principio se pone el if y la condicion y los 2 puntos al 
final, si esa condicion es verdadera va a ejecutar ese pequeño bloque de 
codigo que contiene.
Y si la condicion es Falsa se le puede poner else si no quieres poner otra condicion,
pero si quieres que tenga mas de una sola condicion debes ponerle else if o abreviado seria
elif

Ejemplo de como se estructura si solo quieres que tenga una sola condicion 
if (Condicion):
    pass
else:
    pass

Ejemplo si quieres que tenga mas de una sola condicion 
if (Condicion);
    pass
elif (condicion):
    pass
elif (Condicion):
    pass
else:
    pass

Las condicion ya dependen de ti dee cuantas condiciones quieres que tenga tu codigo
"""
"Calculadora de dscuentos en una tienda"
producto = int(input("Registre el precio de su producto"))

if producto > 1000:
    descuento = producto * 0.150
    producto -= descuento
elif producto > 500:
    descuento = producto * 0.100
    producto -= descuento
else :
    descuento = producto * 0.05
    producto -= descuento
print(f"El precio final con descuento es: {producto}")

"Clasificacion de calificaciones"
"""
Solicita una calificación de 0 a 100.
Si es 90 o más: Excelente
Si es 80 a 89: Muy bien
Si es 70 a 79: Bien
Si es 60 a 69: Suficiente
Menor a 60: Reprobado
"""
""" 
Cálculo de salario semanal
Pide las horas trabajadas y pago por hora.
Si trabajó más de 40 horas, las horas extra se pagan al doble.
Si no, se paga normal.
Muestra el salario total.
"""