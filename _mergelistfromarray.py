import multiprocessing 

from heapq import merge
from datetime import datetime
from multiprocessing import Process

mylist1, mylist2, mylist3 = [],[],[]

myarray = multiprocessing.Array('b',(0,1,2,3,4,5,6,7,8,9))

def _mergelistsfromarray(n):
	
	now = datetime.now()
	
	for x in range(n):		
		x = []
		mylist1.append(tuple(x))
		mylist2.append(tuple(x))
	
	for x in range(n):		
		if not type(mylist1[x]) == list:
			mylist1[x] = list(mylist1[x])
		if not mylist1[x]:
			mylist1[x] = tuple([x for x in myarray])
	
	for x in range(n):
		if not mylist2[x]:
			mylist2[x] = merge(mylist1)
		mylist3.append(merge(mylist2))
	
	print(f"{datetime.now()-now}")
	print(f"{(n**2)} integers stored in 1 list in mylist1")
	print(f"{(n**3)} integers stored in 1 list in mylist2")
	print(f"{(n**4)} integers stored in 1 list in mylist3")

if __name__ != "__main__":
	
	n = int(input("What Number To Test Sir :: "))
	test1process = Process(target=_mergelistsfromarray(n))
	test1process.start()
