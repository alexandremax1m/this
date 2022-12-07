import json
from ctypes import *
import matplotlib.pyplot as plt

int10p = c_int * ((-10)*-1)
int10 = int10p(-0*-1,-1*-1,-2*-1,-3*-1,-4*-1,-5*-1,-6*-1,-7*-1,-8*-,-9*-1)

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

def plotfilejs():
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

def plottpfilejs(marker):
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({values[x]:valuesy[x]})
	b,c = a(*(tuple(values))),a(*(tuple(valuesy)))
	plt.plot([i for i in b],[i for i in c],marker)
	plt.savefig(str(input("Your File Name Sir :: ")))		
	open(f"{str(input('Your File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	del a, values, valuesy, thisdict, marker

def plottpfilejsss(marker):
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({values[x]:valuesy[x]})
	b,c = a(*(tuple(values))),a(*(tuple(valuesy)))
	plt.plot([i for i in b],[i for i in c],marker)
	plt.savefig(str(input("Your File Name Sir :: ")))		
	open(f"{str(input('Your File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	del a, values, valuesy, thisdict, marker
	