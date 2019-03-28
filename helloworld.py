import sys
import os

nombre = input("Nombre ")
c = 0
letter = []
for i in nombre:
    if i not in letter:
        for j in range(0,len(nombre)):
            if i == nombre[j]:
                c+=1
        letter.append(i)
        print(i + " se repite " + str(c) + " vedes")
        c=0

