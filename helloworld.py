import sys
import os

print("Hola...")
Nombre = input("Cual es su nombre? : ")
print("Hola ")
print(Nombre)
for x in Nombre-1:
    rep = 0
    for x in Nombre-1:
        if x == x+1:
            rep += 1
    print(x + "=" + rep)
