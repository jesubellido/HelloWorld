import sys
import os


nombre = input('Enter your name:')
for x in nombre:
	count = 0
	for i in nombre:
		if x == i:
			count += 1	
	print('The letter', x, 'repeats', count, 'time(s)')
# print("HOLA ..."+nombre)
