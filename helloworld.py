name = input()
abc = "abcdefghijklmnopqrstuvwxyz"
contador = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in name:
    for j in range(26):
        if i==abc[j]:
            contador[j]+=1

for k in range(26):
    if contador[k]>0:
        print(abc[k] + ":" + str(contador[k]))

