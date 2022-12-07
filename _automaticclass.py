class MyClassName:
	__slots__ = "mystring","mylist","mydict"
	def __init__(self,mystring,mylist,mydict):
		if type(mystring)==str and type(mylist)==list and type(mydict)==dict:
			self.mystring, self.mylist, self.mydict = mystring, mylist, mydict
		else: 
			datatypes=(str,list,dict)
			myvalues = (mystring, mylist,mydict)
			wrongvalues = []
			for x in range(len(myvalues)):
				if type(myvalues[x]) != datatypes[x]:
					wrongvalues.append({myvalues[x]:datatypes[x]})
			wrongvalues = tuple(wrongvalues)
			for x in wrongvalues:
				print(f"Object could not be initiated because was expecting another datatype for yourinput:expectedtype :: {x}")
			del datatypes, myvalues, wrongvalues

if __name__ != "__main__":
	myclassvars = dir(MyClassName)[25::]
	myclassvars.reverse()
	mysetvars = []
	mysetdatatypes = (str,list,dict)
	for x in range(len(myclassvars)):
		x = mysetdatatypes[x](input(f"Enter Value for {myclassvars[x]} : "))
		if type(x) == list:
			a = int(input("How Many Items To Store In The List"))
			for c in range(a):
				c = input()
				x.append(c)
		if type(x) == dict:
			mydictiniter = []
			a = int(input("How Many Key Value Pairs To Store In This Dict "))
			for c in range(a):
				c1,c2 = input(), input()
				c = [c1,c2]
				mydictiniter.append(c)
			for d in mydictiniter:
				x.update({d[0]:d[1]})
		mysetvars.append(x)
	mysetvars = tuple(mysetvars)
	classvarname = input("Enter Your Object Name :  ")
	classvarname = MyClassName(*mysetvars)
	
				      
