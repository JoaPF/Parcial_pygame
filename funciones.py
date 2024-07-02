import pygame
from pygame import draw
import json



def ordenar_lista_en_dict(datos: dict,nombre_clave_lista: str, clave: str)-> list: 
    "Ordena una lista dentro de un diccionario utilizando burbujeo"
    
    lista = datos[str(nombre_clave_lista)]
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][clave] < lista[j][clave]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista


def guardar_puntajes_json(datos: dict):
    "Exportar a JSON la lista de puntajes"
    
    nombre = datos["puntajes"][0]["nombre"]
    puntaje = datos["puntajes"][0]["puntaje"]

    nuevos_puntajes = {'puntajes':[]}
    nuevos_puntajes['puntajes'].append({"nombre":nombre,"puntaje":puntaje})
    with open('puntajes.json','w') as archivo:
        json.dump(nuevos_puntajes,archivo,indent=4)
    print("Datos exportados")
