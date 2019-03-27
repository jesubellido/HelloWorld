palabra = input("ingrese nombre")
longitud = len(palabra)
contador = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
i=0
j=0

while i<27:
    j=0
    while j<longitud:
       if letras[i]== palabra[j]:
            contador[i]=contador[i]+1

       j+=1
    i+=1


for i in range (0,26,1):
    if contador[i]!=0:
        print(letras[i],"tiene ",contador[i])

