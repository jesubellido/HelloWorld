import sys
import os

print ("Como te llamas?")
nombre = raw_input()

contador=0
for letra in nombre:
    for letrar in nombre:
        if letra==letrar:
             contador+=1
    print(letra+" "+str(contador))
    contador=0

