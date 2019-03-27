import sys
import os

abecedario = "abcdefghijkmnlopqrstuvxyz"

nombre = input("Ingrese su nombre en minusuclas: ")

for letra in abecedario:
    cont = nombre.count(letra)
    if cont > 0:
        print("La letra ", letra, "aparece ", cont, ".")

