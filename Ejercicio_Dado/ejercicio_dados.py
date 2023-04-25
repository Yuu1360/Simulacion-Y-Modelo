"""
Codigo de Apuestas con un dado
Omar Gaspar
Cedula: 28593179
"""
import random

def apuesta():

    numTiradas = 0
    dinero = 100
    
    while dinero >= 100:
        numTiradas += 1
        dinero -= 100
        dinero = dinero + tirar_dado()

    return numTiradas

def tirar_dado():
    dado = random.randrange(1, 6)
    if dado > 3:
        return 200
    else:
        return 0

if __name__ == "__main__":
    promedio = 0
    for i in range(100000):
        promedio += apuesta()
    print(promedio/100000)

