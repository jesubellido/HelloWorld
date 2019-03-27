import sys
import os

sum=0
nombre = raw_input() 
for i in nombre:
    for j in nombre:
        if i==j:
           sum=sum+1
    print(i+" "+str(sum))
    sum=0
