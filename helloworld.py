import sys
import os

nombre = input()
count=0
long = len(nombre)
lista = []
for x in nombre:
    if x in lista:
        continue
    else:
        lista.append(x)
    count2 = 0
    vecesRepetidas = 0
    while count2 < long:
        if x == nombre[count2]:
            vecesRepetidas +=1
        count2 +=1
    print(x + "=" + str(vecesRepetidas))
