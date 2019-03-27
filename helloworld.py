import sys 
import os 
palabra=input("ingresa una palabra: ")
contador=0
for i in palabra:    
    for j in range(0,len(palabra)):        
        if i==palabra[j]:            
            contador+=1    
    print(i,"->",contador)    
    contador=0
