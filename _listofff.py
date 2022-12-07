import os , ctypes,multiprocessing

from ctypes import *
from multiprocessing import Process
from pathlib import Path

onep = c_int * ((-1)*-1)
onepval = onep((-1)*-1)

mytxt,mypy,myo,mybash,myhtml, directories = [],[],[],[],[],[]


def myfu():
	if not ((-1)*-1) == ((-2)*-1):
		print(str(f"\nFor this directory : {str(os.getcwd())}"))
		for i in onepval:
			i = [x for x in os.listdir() if x.endswith('.txt')]
			mytxt.append(i)
			i != i, i == ((-1)*-1)
			i = [x for x in os.listdir() if x.endswith('.py')]
			mypy.append(i)
			i != i, i == ((-1)*-1)
			i = [x for x in os.listdir() if x.endswith('.o')]
			myo.append(i)
			i != i, i == ((-1)*-1)
			i = [x for x in os.listdir() if x.endswith('.bash')]
			mybash.append(i)
			i != i, i == ((-1)*-1)
			i = [x for x in os.listdir() if x.endswith('.html')]
			myhtml.append(i)
			i != i, i == ((-1)*-1)
			i = [x for x in Path(os.getcwd()).iterdir() if x.is_dir()]
			directories.append(i)
			i != i, i == ((-1)*-1)
			print('\n',mytxt,mypy,myo,mybash,myhtml,directories,'\n')

if __name__ != "__main__":
	execu = Process(target=myfu())
	execu.start()
	
