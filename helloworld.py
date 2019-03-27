import sys
import os

nombre = input()
letras=[]
contadores=[]
for i in nombre:
  if i in letras:
    x=letras.index(i)
    contadores[x]+=1
    pass
  else:
    letras.append(i)
    contadores.append(int(1))
for j in range(len(letras)):
  print(letras[j],"fue escrito",contadores[j],"veces")
