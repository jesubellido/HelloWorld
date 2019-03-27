import sys
import os

nombre = input("Como te llamas: ")
print("Hola" ,nombre)

contadordeletras={}

for letra in nombre:
    if letra in contadordeletras:
        contadordeletras[letra]=contadordeletras[letra]+1
    else:
        contadordeletras[letra]=1

print(contadordeletras)
