import sys
import os

word=input("Ingresa la palabra: ")

list=[];
for e in word:
	cant=0
	for i in word:
		if e == i:
			cant+=1
	list.append(e)
	print(e,"->",cant)