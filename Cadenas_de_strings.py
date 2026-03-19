#Variables y tipo str (string) o cadena de texto 
"""
18 de Marzo del 2026
Para que funciona las comillas doble, simple, 
Triple comilla doble y triple comilla simple
"""
Cadena_uno = "Hola" #comilla doble
Cadena_dos = 'Como' #comilla simple
"""
Las comillas dobles siven para hacer una sola palabra lineal 
ya que no puedes darle un enter para seguir escribiendo abajo 
por que sino te va marcar un error.
Esto tambien aplica para las comillas simples
"""
Cadena_tres = """estas """ #triple comilla doble
cadena_cuatro = '''
mi primer texto en python
    hola
        Estamos aburridos
''' # triple comilla simple
"""
La triple comilas doble nos sirven para hacer textos 
mas largos y a estos si se les permiten hacer varios espaciados
como el que estan leyendo ahora.
Esto tambien aplica para las triples comillas simples
"""
Nombre = 'David'
edad = 25
edad_str = str(edad) # estos el 25 convertido a string

print(Cadena_uno+ " " + Cadena_dos+" "+ Cadena_tres)
print(Nombre + " " + edad_str) #concatenacion 
print(f"{Nombre}, edad {edad} ")
