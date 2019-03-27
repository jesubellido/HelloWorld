import sys
import os

dict = {}
nombre = input("Ingresar nombre: ")
print("HOLA ..."+nombre)
for letter in nombre:
    if letter in dict.keys():
        dict[letter] = dict.get(letter) + 1    
    else:
        dict[letter] = 1

for key in dict:
    print(key + " --> " + str(dict[key]))

