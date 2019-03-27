import sys
import os

nombre = input("Cual es tu nombre : ")
print("Hola ",nombre)

cuenta={}

for caracter in nombre:
  if caracter in cuenta:
    cuenta[caracter]=cuenta[caracter]+1
  else:
    cuenta[caracter]=1 
  
print(cuenta)
