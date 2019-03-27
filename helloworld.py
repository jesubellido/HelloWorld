import sys
import os
i=0
Lista=[]
Listalimpia=[]
nombre = input("Ingresa tu nombre: ")
while i<len(nombre):
    Lista.append(nombre[i])
    i+=1
for j in Lista:
    if j not in Listalimpia:
        Listalimpia.append(j)
for g in Listalimpia:
    print("La letra ",g, " aparece ",nombre.count(g), " veces")


#Escrito por Fabrizio Franco utilizando PYTHON 3 (ejecutar con dicha version)
