import sys
import os

nombre = input("Como te llamas?")
c = 0
for i in nombre:
    if i != " ":
       c=c+1
print (c)
