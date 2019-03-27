import sys
import os

nombre =raw_input("Como te llamas?")
contador = 0
letra = ""
for c in nombre:
    for j in nombre:
        if c==j:
            contador += 1
    contador=0
    print(c+" se repite "+str(contador)+" veces." )



