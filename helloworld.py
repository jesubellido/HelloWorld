import sys
import os
sum=0
nombre = input()
for i in nombre:
    for j in nombre:
        if i==j:
           sum=sum+1
    print(i," ",sum)
    sum=0
