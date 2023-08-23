"""
Materia: Laboratorio de Datos
Arbolado en los espacios verdes de CABA
Autores: Agustin Russo, Gabo, Lucas
Descripcion:...
Fecha de Creacion: 21/08/2023
Fecha de Finalizacion: ...
"""
import csv
path_csv = "arbolado-en-espacios-verdes.csv"

#Ejercicios

#1
def leer_parque(archivo: csv, parque: str)->list[dict]:
    lista_arboles = []
    with open(archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            if fila[10] == parque:
                lista_arboles.append(dict(zip(encabezado,fila)))
    return lista_arboles

#print(leer_parque(path_csv, "GENERAL PAZ"))

#2
"""def especies(lista_arboles: list[dict])->list:
    ejemplares = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] in ejemplares:
            continue
        else:
            ejemplares.append(arbol['nombre_com'])
    return ejemplares
"""
def especies(lista_arboles: list[dict])->list:
    ejemplares = []
    for arbol in lista_arboles:
        if not arbol['nombre_com'] in ejemplares:
            ejemplares.append(arbol['nombre_com'])
    return ejemplares
   

#print(especies(leer_parque(path_csv, "GENERAL PAZ")))

#3
def contar_ejemplares(lista_arboles: list[dict])->dict:
    cant_ejemplares = {}
    for arbol in lista_arboles:
        if not arbol['nombre_com'] in cant_ejemplares:
            cant_ejemplares[arbol['nombre_com']]=1
        else:
            cant_ejemplares[arbol['nombre_com']]+=1
    return cant_ejemplares

print(contar_ejemplares(leer_parque(path_csv,"ANDES, LOS")))

#4
def obtener_alturas(lista_arboles: list[dict], especie: str)->list[float]:
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas


def promedio_max(alturas: list[float])->list[float]:
    max = 0
    suma = 0
    for altura in alturas:
        suma += altura
        if altura>=max:
            max=altura
    prom = suma/len(alturas)
    return [max,prom]

"""print(promedio_max(obtener_alturas(leer_parque(path_csv,"GENERAL PAZ"), 'Jacarandá')))
print(promedio_max(obtener_alturas(leer_parque(path_csv,"ANDES, LOS"), 'Jacarandá')))
print(promedio_max(obtener_alturas(leer_parque(path_csv,"CENTENARIO"), 'Jacarandá')))"""


#5
def obtener_inclinaciones(lista_arboles:list[dict], especie: str)-> list[float]:
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            inclinaciones.append(arbol["inclinacio"])
    return inclinaciones

#6
def especimen_mas_inclinado(lista_de_arboles)-> list[str,float]:
    lista_especies = especies(lista_de_arboles)
    especie_max = [str, 0.0]
    for i in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_de_arboles, i)
        inclinacion_max = 0
        for e in inclinaciones:
            if e > inclinacion_max:
                inclinacion_max = e
        if inclinacion_max > especie_max[1]:
            especie_max[0], especie_max[1] = i, inclinacion_max
    return especie_max
#print(especimen_mas_inclinado())
