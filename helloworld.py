import sys 
import os 
nombre=input("Ingrese su nombre: ")
longitud=len(nombre)
letras=[]

for i in range(0,longitud,1):
    letras.append(nombre[i])
for j in range(0,longitud,1):
    a= nombre[j]
    b=0
    for k in range(0,longitud,1):
        if a == nombre[k]:
            b=b+1
    print("La letra ", nombre[j] ," se repite ", b ,"veces")






