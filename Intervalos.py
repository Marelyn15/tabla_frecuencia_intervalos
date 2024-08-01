from intervaltree import Interval

def intervalos(inicio, fin, tamaño):
    intervalos = []
    while inicio < fin:
        intervalos.append(Interval(inicio, inicio + tamaño))
        inicio += tamaño
    return intervalos

#Datos a utilizar
intervals = intervalos(60,75,3)
datos_ord_intervalos = [5,18,42,27,8] #Ni o frecuencia


def tabla_frecuencia_intervalos(intervals,datos_ord_intervalos):

    #Datos a utilizar
    print("Estos son los intervalos ",intervals)
    print("Estos son las frecuencias originales (ni)",datos_ord_intervalos) #ni

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
    print(f"Frecuencia Absoluta acumulada (Ni) {Ni}")

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

tabla_frecuencia_intervalos(intervals,datos_ord_intervalos)

"""
mediana = st.median(marca_clase)
print(mediana)
moda = st.mode(marca_clase)
print(moda)
"""