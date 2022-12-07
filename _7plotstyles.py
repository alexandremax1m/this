import json
from ctypes import *

import matplotlib.pyplot as plt

int10p = c_int * ((-10)*-1)
int10 = int10p(-0*-1,-1*-1,-2*-1,-3*-1,-4*-1,-5*-1,-6*-1,-7*-1,-8*-1,-9*-1)

def autoplot():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({str(values[x]):valuesy[x]})
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	plt.plot([i for i in b],[i for i in c],'o')
	plt.savefig(str(input("Your Image Name Sir :: ")))		
	open(f"{str(input('Your Json Output File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	plt.show()

def autoscatter():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({str(values[x]):valuesy[x]})
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	plt.scatter([i for i in b],[i for i in c])
	plt.savefig(str(input("Your Image Name Sir :: ")))		
	open(f"{str(input('Your Json Output File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	plt.show()

def autobar():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy,thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({str(values[x]):valuesy[x]})
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	plt.bar([i for i in b],[i for i in c])
	plt.savefig(str(input("Your Image Name Sir :: ")))		
	open(f"{str(input('Your Json Output File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	plt.show()

def autostem():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({str(values[x]):valuesy[x]})
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	plt.stem([i for i in b],[i for i in c])
	plt.savefig(str(input("Your Image Name Sir :: ")))		
	open(f"{str(input('Your Json Output File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	plt.show()

def autostep():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({str(values[x]):valuesy[x]})
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	plt.step([i for i in b],[i for i in c])
	plt.savefig(str(input("Your Image Name Sir :: ")))		
	open(f"{str(input('Your Json Output File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	plt.show()
	
def autofill():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, valuesy2, thisdict = [],[],[],{}
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		valuesy2.append(int(input(f'At Pointer Address a, 1 list values, Y2 Coordinates, value {x} Sir :: ')))
		thisdict.update({str(values[x]):{valuesy[x]:valuesy2[x]}})
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	d = a(*(tuple(valuesy2)))
	plt.fill_between([i for i in b],[i for i in c],[i for i in d])
	plt.savefig(str(input("Your Image Name Sir :: ")))		
	open(f"{str(input('Your Json Output File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	plt.show()

def autostack():
	a = c_int * (int(input('How Many Values The Pointer Hast To Tell The Memory Address To Save Sir :: ')))
	values, valuesy, thisdict = [],[]
	for x in range(int(input('How Many Values To Create Sir, Remember Your At Pointer Address a Sir :: '))):
		values.append(int(input(f'At Pointer Address a, 1 list values, X Coordinates, value {x} Sir :: ')))
		valuesy.append(int(input(f'At Pointer Address a, 1 list values, Y Coordinates, value {x} Sir :: ')))
		thisdict.update({str(values[x]):valuesy[x]})
	b = a(*(tuple(values)))
	c = a(*(tuple(valuesy)))
	plt.stackplot([i for i in b],[i for i in c])
	plt.savefig(str(input("Your Image Name Sir :: ")))		
	open(f"{str(input('Your Json Output File Name Sir :: '))}","w+",encoding='UTF-8').write((json.dumps(thisdict,sort_keys=True, indent=4)))
	plt.show()		