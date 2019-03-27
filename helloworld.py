import sys
import os


abcd = "abcdefghijklmnopqrstuvwxyz"

nombre = input("Ingrese su nombre en minusculas: ")


for caracter in abcd:
    contador = nombre.count(caracter)
    if contador > 0:
        print("La letra ",caracter," se repite ",contador, ".")
