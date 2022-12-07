from ctypes import *
import matplotlib.pyplot as plt


cp,rp = c_int * (-1*-1), c_int * (-1*-1)
cn,rn = int(input('Columns Number Sir :: ')), int(input('Rows Number Sir :: '))
ip,thislist = c_int * (-(cn)*-(rn)), [x+1 for x in range(cn*rn)]
index = ip(*(tuple(thislist)))

for i in index:
	plotax, plotyx = [],[]
	for x in range(int(input('How Many Values For YX axes Sir :: '))):
		plotax.append(int(input(f'Your X Coordinate {x} Sir ::')))
		plotyx.append(int(input(f'Your Y Coordinate {x} Sir ::')))
	axp, yxp = c_int * (-(int(len(plotax)))*-1), c_int * (-(int(len(plotyx)))*-1)
	axx, yxx = axp(*(tuple(plotax))), yxp(*(tuple(plotyx)))
	a_i = plt.subplot(int(f"{cn}{rn}{i}")).plot([i for i in axx],[i for i in yxx])
	a_i = plt.subplot(int(f"{cn}{rn}{i}")).stem([i for i in axx],[i for i in yxx])
	del plotax,plotyx,axp,yxp,axx,yxx

plt.show()




	


