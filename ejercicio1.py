a = input("Dame tu nombe: ")
k = len(a)
for i in range(0,k):
    contador = 0
    for j in range(0,k):
        if(a[i]==a[j]):
            contador = contador+1
    print(a[i], "se repite ",contador," veces")


