import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Raíz cuadrada de un número negativo"

# Prueba de las funciones
print("Suma: ", sumar(5, 3))
print("Resta: ", restar(5, 3))
print("Multiplicación: ", multiplicar(5, 3))
print("División: ", dividir(5, 3))
print("Raíz cuadrada: ", raiz_cuadrada(9))