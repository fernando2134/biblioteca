'''
Curso Backend de Python 2022
Ejercicios Prácticos
1. Realice las funciones necesarias para que retornen los siguientes resultados:
a. El área de un triángulo rectángulo.
b. El perímetro de un cuadrado.
c. El volumen de una esfera.
d. El volumen de un cilindro.
2. Escribir una función que calcule el máximo común divisor entre dos números.
3. Escribir una función que calcule el mínimo común múltiplo entre dos números
4. Escribir una función que reciba una cadena de caracteres y devuelva un
diccionario con cada palabra que contiene y la cantidad de veces que aparece
(frecuencia).
5. Escribir una función que reciba el diccionario generado con la función de la
consigna anterior y devuelva una tupla con la palabra más repetida y su
frecuencia.
'''
import math


# punto1
def area_triangulo(base, altura):
    return base * altura / 2


def per_cudrado(lado):
    return 4 * lado


def volumen_esfera(radio):
    volumen = (4 / 3) * math.pi * radio ** 3
    return volumen


def volumen_cilindro(radio, altura):
    volumen = math.pi * radio ** 2 * altura
    return volumen


# punto2

def maximo_comun_divisor(a, b):
    resto = 0

    while b > 0:
        resto = b

        b = a % b

        a = resto

    return a


# punto3
def minimo_comun_multiplo(n1, n2):
    a = max(n1, n2)
    b = min(n1, n2)
    mcm = (a / maximo_comun_divisor(a, b)) * b
    return mcm
# punto4

def creador_dict(cadena):
  '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
  lista_1= cadena.split()
  dict_1={}
  for i in list_1:
    if i in dict_1:
      dict_1[i] +=1
    else:
      dict_1[i]= 1
  return dict_1

def contador_dict(dictionario):
  '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
  palabra_frecuente= ''
  cantidad=0
  for keys,values in dictionario.items():
    if values > cantidad:
      cantidad= values
      palabra_frecuente= keys
  return palabra_frecuente,cantidad
entrada=input('Ingrese su cadena de caracteres: ')
print(creador_dict(entrada))
print(contador_dict(creador_dict(entrada)))

# punto5