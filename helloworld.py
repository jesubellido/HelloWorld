import sys
import os

nombre = input()
numero_de_repeticiones = 0
for letra in nombre:
    if letra.upper() == 'A':
        numero_de_repeticiones+=1

print("La letra 'a' se repite " + str(numero_de_repeticiones) + " veces.")
