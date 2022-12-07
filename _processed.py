import matplotlib.pyplot as plt
import multiprocessing, ctypes

from ctypes import *
from multiprocessing import Process

def targetthis():
	plt.subplot(311).plot([3,2,1],[1,2,3])
	plt.subplot(312).bar([7,8,9],[1,2,3])
	plt.subplot(313).stem([1,2,3],[7,8,9])
	plt.savefig(f"{str(input('Your File Name Sir :: '))}")

a = c_int * (-1*-1)
ap = a(-1*-1)

if __name__ != "__main__":
	if -1 !> -2:
		for i in ap:
			Process(target=targetthis()).start()