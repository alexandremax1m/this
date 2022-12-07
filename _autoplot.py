import json
from ctypes import *
import matplotlib.pyplot as plt

def autoplot():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy = [],[]
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	thisdict = {}
	plt.plot([i for i in b],[i for i in c],'o')
	plt.show()

def autoplotwjs():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({values[x]:valuesy[x]})
	b,c = a(*(tuple(values))),a(*(tuple(valuesy)))
	plt.plot([i for i in b],[i for i in c],'o')
	plt.savefig(str(input("Your File Name Sir :: ")))		
	open(f"{str(input('Your File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	