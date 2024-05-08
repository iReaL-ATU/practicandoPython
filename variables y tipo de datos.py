edad = 24 # número entero (integer)
precio = 112.9 # número de punto flotante (float)
titulo = 'Aprende Python desde cero' # cadena de texto (string)
test = True # booleano

# Los nombres de las variables son case sensitive, es decir, no es lo mismo que una variable se llame resultado que RESULTADO.

# Utilizar nombres descriptivos, en minúsculas y separados por guiones bajos si fuese necesario: resultado, mi_variable, valor_anterior,...

# Escribir las constantes en mayúsculas: MI_CONSTANTE, NUMERO_PI, ...

#-------------------------------------------------------------------
#Lectura de datos en Python
nombre = input("Escribe tu nombre: ")
print(nombre)

n1 = int(input("Escribe un numero: "))
n2 = int(input("Escribe un numero: "))

print(n1+n2)
#-------------------------------------------------------------------
# Números
# Python soporta dos tipos de números: enteros (integer) y de punto flotante (float).

# integer
x = 5

# float
y = 5.0

# Otra forma de declarar un float
z = float(5)

#Funcion type() que tipo de variable es
x = 5.5
print(type(x))

#-------------------------------------------------------------------
# Cadenas de texto (string)
# Las cadenas de texto o strings se definen mediante comilla simple (' ') o doble comilla (" "):

mi_nombre = 'Ane'
print(mi_nombre)
mi_nombre= "Ane"
print(mi_nombre)

# Para definir strings multi-línea se utiliza la triples comillas ("""):

frase = """ esto es una
        frase muy larga de más de
        una línea ..."""
