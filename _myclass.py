import ctypes
from ctypes import *

a = c_short * 10
b = a(0,1,2,4,5,6,7,8,9)

mytextvariable = "asdasdasd1"

c = c_char * 10

# fix () ## it is okay
b = input(c(tuple([].append(str(input((bytes(x),encoding='UTF-8')))).append(x) for x in input()))))

b = input(c(bytearray(tuple([].append(bytes(x,encoding='UTF-8') for x in str(input("Your Char Arr Sir : ")))), encoding = 'UTF-8')))

class MyClassName(Structure):
	_fields_ = [("arrayoften",b),("pointeraddress",]