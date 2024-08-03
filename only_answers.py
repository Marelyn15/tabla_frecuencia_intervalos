from intervaltree import Interval
from collections import Counter
import statistics as st
import Intervalos as Itvl

#---------------------------------Datos a partir de una lista -------------------------------------------------

#Para sacar el valor maximo y minimo de una mejor manera
grupo = [60,66,77,70,66,68,57,70,66,52,75,65,69,71,58,66,67,74,61,63,69,80,59,66,70,67,78,75,64,71,81,62,64,69,68,72,83,56,65,74,67,54,65,65,69,61,67,73,57,62,67,68,63,67,71,68,76,61,62,63,76,61,67,67,64,72,64,73,79,58,67,71,68,59,69,70,66,62,63,66]
#Inicio del intervalo se disminuirá hacia el cero o cinco más cercano ejemplo 52, el inicio es 50
#Fin del intervalo se elevará hacia el cero o cinco mas cercano, ejemplo 83, el fin es 85 
print(f"El valor mas pequeño del grupo es {min(grupo)}. El valor más grande es {max(grupo)}")

def intervalos(inicio, fin, tamaño):
    intervalos = []
    while inicio < fin:
        intervalos.append(Interval(inicio, inicio + tamaño))
        inicio += tamaño
    return intervalos

saltos = intervalos(50,85,5)

# Función para mapear cada número al intervalo correspondiente
def mapeo_intervalos(grupo, saltos):
    mapeo = []
    for numero in grupo:
        for salto in saltos:
            # El intervalo [inicio, fin) incluye inicio pero excluye fin
            if salto.begin <= numero < salto.end: #Se toma la variable salto que se crea en el for.
                mapeo.append(salto)
                break
    return mapeo


mapeo = mapeo_intervalos(grupo,saltos)
FA = Counter(mapeo)
FA = dict(sorted(FA.items()))
#print(FA)

datos_ord_intervalos = [] #Clave Individual
#Valores de la clave individual
for index, valor in enumerate(FA.values()):
    datos_ord_intervalos.insert(index,valor)
#print(datos_ord_intervalos)


Itvl.tabla_frecuencia_intervalos(saltos,datos_ord_intervalos)


#-----------------------Datos estáticos ---------------------------------------------
#Datos a utilizar
#intervals = intervalos(60,75,3)
#Cuando los datos son estáticos
#datos_ord_intervalos = [5,18,42,27,8] #Ni o frecuencia

intervals = intervalos(0,80,20)
#Cuando los datos son estáticos
datos_ord_intervalos = [45,10,5,2] #Ni o frecuencia

#Itvl.tabla_frecuencia_intervalos(intervals,datos_ord_intervalos)