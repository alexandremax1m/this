from datetime import datetime
from array import *

myarrayresults, mylistresults = {}, {}

def _try_fromlist(n):
	now = datetime.now()
	mylist = [x for x in range(n)]
	for x in mylist:
		print(x)
	mylistresults.update({n:datetime.now()-now})

def _try_fromarray(n):
	if n <= 255:
		mytpcode = 'b'
	elif 255 < n <= 65535:
		mytpcode = 'i'
	elif 65535 < n <= 4294967295:
		mytpcode = 'I'
	now = datetime.now()
	myarray = array(mytpcode,[x for x in range(n)])
	for x in myarray:
		print(x)
	myarrayresults.update({n:datetime.now()-now})

### list of lists from array is faster than for x in range(x)

results2, results22, listresults2,bigresults = {},{},{},{}

def _listoflistsfromarray(n):
	now = datetime.now()
	mylistsoflist = []
	myarray = array('b',[x for x in range(10)])
	listsinsidelist = [x for x in myarray]*n
	mylistsoflist.append(listsinsidelist)
	print(mylistsoflist)
	results2.update({n*10:datetime.now()-now})

def _biglistfromarrayelem(n):
	now = datetime.now()
	myarray = array('b',[x for x in range(10)])
	myemptylist = []
	for x in range(n):
		x = []
		myemptylist.append(x)
	for x in range(n):
		myemptylist[x] = [x for x in myarray]
	print(myemptylist)
	bigresults.update({n:datetime.now()-now})

def _listoflistsfromarray2(n):
	now = datetime.now()
	mylistsoflist = []
	myarray = array('b',[x for x in range(10)])
	listsinsidelist = [x for x in myarray]*n
	mylistsoflist.append(listsinsidelist)
	mylistsoflist = tuple(mylistsoflist)
	print(mylistsoflist)
	results22.update({n*10:datetime.now()-now})

def _randomlistgenerator(n):
	now = datetime.now()
	mylist = [ x for x in range(n) ]
	print(mylist)
	listresults2.update({n:datetime.now()-now})
	




	
	
	