import matplotlib, numpy, ctypes

from numpy import *
from matplotlib import pyplot

from matplotlib.pyplot import plot
from matplotlib.pyplot import scatter
from matplotlib.pyplot import stem
from matplotlib.pyplot import step
from matplotlib.pyplot import stackplot

from matplotlib.pyplot import bar
from matplotlib.pyplot import fill_between

from datetime import datetime
from multiprocessing import Process

from ctypes import *

ap = c_int * 5
aap = ap(0,1,2,3,4)

pp = c_int * ((-1)*-1)
ppp = pp((-1)*-1)

thislist = []

for i in aap:
	thislist.append([])
	if not thislist[i]:
			if i %2 == 0:
				thislist[i] = [2,4,6,8,10]
			else:
				thislist[i] = [1,2,5,14,3]
def createtest():
	for i in aap:
		if i == 0:
			pyplot.plot(numpy.array(thislist[i]),numpy.array(thislist[i+1]))
			pyplot.savefig(f"plot{i}.jpeg")
		elif i == 1:
			pass
		elif i == 2:
			pyplot.scatter(numpy.array(thislist[i]),numpy.array(thislist[i+1]))
			pyplot.savefig(f"scatter{i}.jpeg")
		elif i == 3:
			pass
		elif i == 4:
			pyplot.step(numpy.array(thislist[i-1]),numpy.array(thislist[i]))
			pyplot.savefig(f"step{i}.jpeg")

def create5plot():
	this = []
	for i in aap:
		this.append([])
		if not this[i]:
			this[i] =[[],[]] 
			thismuch = int(input('How Many XY Coordinates Sir :: '))
			for x in range(thismuch):
				this[i][0].append((int(input(f"Your {x} X Coordinate Value Sir :: "))))
			for x in range(thismuch):
				this[i][1].append((int(input(f"Your {x} Y Coordinate Value Sir :: "))))
		for x in range(int(len(this))):
			pyplot.plot(numpy.array(this[x][0][0]),numpy.array(this[x][0][1]))
			pyplot.savefig(str(input("Your File Name Sir :: ")))

# now this goes like for i in aap: if %2 :: do this

if not __name__ == "__main__":
	now = datetime.now()
	for i in ppp:
		i = Process(target=create5plot())
		i.start()
	print(datetime.now()-now)		