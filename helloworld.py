import sys
import os

nombre = input()
numero_de_letras = {}
for letra in nombre:
    if letra.upper() in numero_de_letras:
        numero_de_letras[letra.upper()]+=1
    else:
        numero_de_letras[letra.upper()] = 1

for letra in numero_de_letras:
    print("La letra " + letra + " se repite " + str(numero_de_letras[letra]) + " veces.")
