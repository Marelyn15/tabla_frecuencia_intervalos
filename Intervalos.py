from intervaltree import Interval
import statistics as st
import math

def intervalos(inicio, fin, tamaño):
    intervalos = []
    while inicio < fin:
        intervalos.append(Interval(inicio, inicio + tamaño))
        inicio += tamaño
    return intervalos

#Datos a utilizar
intervals = intervalos(60,75,3)
datos_ord_intervalos = [5,18,42,27,8] #Ni o frecuencia

#Total de datos ordenados por intervalo
total_ord_intervalos = sum(datos_ord_intervalos)

#Mitad
mitad = total_ord_intervalos / 2

#Punto medio
marca_clase = []
for index, valor in enumerate(intervals):
    div = (valor[0] + valor[1]) / 2
    marca_clase.insert(index,div)

print('Estas son las marchas de clase', marca_clase)

#Xi Ni multiplicacion marca clase y frecuencia
Xi_Ni = []
for index, valor in enumerate(marca_clase):
    mult = valor * datos_ord_intervalos[index]
    Xi_Ni.insert(index,mult)

print('Puntos medios por frecuencia', Xi_Ni)

#Total Xi Ni 
total_Xi_Ni = sum(Xi_Ni)
print("Este es el total de la multiplicacion de puntos medios por frecuencia", total_Xi_Ni)

#Media para Xi Ni (Exclusivo intervalos)
Media_Xi_Ni = total_Xi_Ni/total_ord_intervalos
print("Media para Xi Ni ", Media_Xi_Ni)