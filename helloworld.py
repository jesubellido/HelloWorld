import sys
import os

nombre=input()
suma=0
for i in nombre:
    for j in nombre:
        if i == j:
            suma=suma+1
    print(i, suma)
    suma=0
