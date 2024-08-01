from intervaltree import Interval
from collections import Counter

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

#Datos ejercicio 1
intervalo = intervalos(50,85,5)
print("Los intervalos son ", intervalo)

# Función para mapear cada número al intervalo correspondiente
def mapeo_intervalos(grupo, intervalos):
    mapeo = []
    for numero in grupo:
        for intervalo in intervalos:
            # El intervalo [inicio, fin) incluye inicio pero excluye fin
            if intervalo.begin <= numero < intervalo.end:
                mapeo.append(intervalo)
                break
    return mapeo


mapeo = mapeo_intervalos(grupo,intervalo)
FA = Counter(mapeo)
FA = dict(sorted(FA.items()))
#print(FA)

datos_ord_intervalos = [] #Clave Individual
#Valores de la clave individual
for index, valor in enumerate(FA.values()):
    datos_ord_intervalos.insert(index,valor)
#print(datos_ord_intervalos)

#Datos a utilizar
#intervals = intervalos(60,75,3)
#Cuando los datos son estáticos
#datos_ord_intervalos = [5,18,42,27,8] #Ni o frecuencia


def tabla_frecuencia_intervalos(intervals,datos_ord_intervalos):

    #Datos a utilizar
    print("Estos son los intervalos ",intervals)
    print("Estos son las frecuencias originales (ni) o (FA)",datos_ord_intervalos) #ni

    #Total de datos ordenados por intervalo
    total_ord_intervalos = sum(datos_ord_intervalos)

    #Mitad
    mitad = total_ord_intervalos / 2
    print('Mitad o media de la clase es', mitad)

    #Punto medio
    marca_clase = []
    for index, valor in enumerate(intervals):
        div = (valor[0] + valor[1]) / 2
        marca_clase.insert(index,div)

    print('Estas son las marcas de clase (Xi)', marca_clase)

    #Xi Ni multiplicacion marca clase y frecuencia
    Xi_Ni = []
    for index, valor in enumerate(marca_clase):
        mult = valor * datos_ord_intervalos[index]
        Xi_Ni.insert(index,mult)

    print('Puntos medios por frecuencia (Xi ni)', Xi_Ni)

    #Total Xi Ni 
    total_Xi_Ni = sum(Xi_Ni)
    print("Este es el total de la multiplicacion de puntos medios por frecuencia ", total_Xi_Ni)

    #Media para Xi Ni (Exclusivo intervalos)
    Media_Xi_Ni = total_Xi_Ni/total_ord_intervalos
    print("Media para Xi Ni ", Media_Xi_Ni)

    #Frecuencia absoluta acumulada o Ni
    nuevo_valor = 0
    Ni = []
    for index, valor in enumerate(datos_ord_intervalos): 
        nuevo_valor = valor + nuevo_valor
        Ni.insert(index,nuevo_valor)
    print(f"Frecuencia Absoluta acumulada (Ni) o (FAA) {Ni}")

    def encontrar_numero_cercano(numero, lista):
        numero_cercano = lista[0]
        indice_cercano = 0
        diferencia_minima = abs(numero - numero_cercano) 

        for i in range(1,len(lista)):
            diferencia_actual = abs(numero - lista[i])
            if diferencia_actual < diferencia_minima:
                numero_cercano = lista[i]
                indice_cercano = i
                diferencia_minima = diferencia_actual
        return numero_cercano, indice_cercano


    numero_cercano_media, indice_datos_centralizados = encontrar_numero_cercano(mitad,Ni)

    #Valores a utilizar para las operaciones
    indice_valor_indicado = intervals[indice_datos_centralizados] #Seleccion de la clase 
    Li = indice_valor_indicado[0] #Limite inferior de la mediana
    Ni_clase_anterior = Ni[indice_datos_centralizados - 1] #Frecuencia absoluta acumulada de la clase anterior
    FAM = datos_ord_intervalos[indice_datos_centralizados] #Frecuencia absoluta de la clase de la mediana (este caso de la que elegimos)
    FAM_clase_anterior = datos_ord_intervalos[indice_datos_centralizados - 1] #Frecuencia absoluta de la clase anterior
    FAM_clase_siguiente = datos_ord_intervalos[indice_datos_centralizados + 1] #Frecuencia absoluta de la clase anterior
    Ti = len(indice_valor_indicado) #El tamaño del intervalo

    #Mediana o me
    me =  round(Li + ((mitad - Ni_clase_anterior)/FAM) * Ti,2)
    print("Este es el valor de la mediana ", me)

    #Moda o mo 
    mo = round(Li + ((FAM - FAM_clase_anterior)/((FAM - FAM_clase_anterior) + (FAM - FAM_clase_siguiente))) * Ti,2)
    print("Este es el valor de la moda ", mo)

tabla_frecuencia_intervalos(intervalo,datos_ord_intervalos)
#tabla_frecuencia_intervalos(intervals,datos_ord_intervalos)

