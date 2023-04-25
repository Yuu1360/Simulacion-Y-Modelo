"""
Codigo de Apuestas con un dado
Omar Gaspar
Cedula: 28593179
"""

import csv
import statistics

datos = []
with open('Ejercicio_Promedio_y_Moda/datos.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        datos.append(row)

def promedioEdades():
    edades = []
    for row in datos:
        edades.append(int(row['edad']))
    return statistics.mean(edades)

def modaEdades():
    edades = []
    for row in datos:
        edades.append(int(row['edad']))
    return statistics.mode(edades)

if __name__ == "__main__":
    
    print(promedioEdades())
    print(modaEdades())