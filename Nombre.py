nombre = input("Ingresa tu nombre: ")
indice = 0
indice2 = 0
while indice < len(nombre):
    letra = nombre[indice]
    while indice2 < len(nombre):
        contador = 0
        if(letra == nombre[indice2]):
            contador += 1
            print(letra)
            print(contador)
            indice2 += 1
    indice += 1        
