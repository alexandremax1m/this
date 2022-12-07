import os, subprocess, re
import multiprocessing, ctypes

from multiprocessing import *
from multiprocessing import Process
from ctypes import *

## control flow

find_jmp = re.compile(r".{0,200}jmp.{0,100}")

## bitwise

find_or = re.compile(r".{0,200}or.{0,100}")
find_xor = re.compile(r".{0,200}xor.{0,100}")
find_and = re.compile(r".{0,200}and.{0,100}")
find_not = re.compile(r".{0,200}not.{0,100}")

## shift left shift right

find_shl = re.compile(r".{0,200}shl.{0,100}")
find_shr = re.compile(r".{0,200}shr.{0,100}")

## data movement

find_push = re.compile(r".{0,200}push.{0,100}")
find_pop = re.compile(r".{0,200}push.{0,100}")
find_mov = re.compile(r".{0,200}mov.{0,100}")
find_lea = re.compile(r".{0,200}lea.{0,100}")

## aritmetic operations

find_add = re.compile(r".{0,200}add.{0,100}")
find_sub = re.compile(r".{0,200}sub.{0,100}")
find_inc = re.compile(r".{0,200}inc.{0,100}")
find_dec = re.compile(r".{0,200}dec.{0,100}")
find_imul = re.compile(r".{0,200}imul.{0,100}")
find_idiv = re.compile(r".{0,200}idiv.{0,100}")
find_neg = re.compile(r".{0,200}neg.{0,100}")

## registers
find_register1 = re.compile(r".{0,200}edx.{0,100}")
find_register2 = re.compile(r".{0,200}eax.{0,100}")
find_register3 = re.compile(r".{0,200}ebx.{0,100}")
find_register4 = re.compile(r".{0,200}ecx.{0,100}")
find_register5 = re.compile(r".{0,200}esi.{0,100}")
find_register6 = re.compile(r".{0,200}edi.{0,100}")
find_register7 = re.compile(r".{0,200}esp.{0,100}")
find_register8 = re.compile(r".{0,200}ebp.{0,100}")

def this():

	for x in os.listdir():
		if x.endswith('.o'):
			a = subprocess.run(["objdump","-D",f"{x}"],text=True, capture_output=True)
			with open(f"{x[0:5]}.txt","a+") as file_fu:
				file_fu.write(a.stdout)
			b = subprocess.run(["objdump","-a",f"{x}"],text=True, capture_output = True)
			with open(f"{x[0:5]}.txt","a+") as file_fu:
				file_fu.write(b.stdout)

	for x in os.listdir():
		if x.endswith('.txt'):
			a = [re.findall(find_xor,line) for line in open(f"{x}","r",encoding='UTF-8')]
			b = [re.findall(find_push,line) for line in open(f"{x}","r",encoding='UTF-8')]
			c = [re.findall(find_add,line) for line in open(f"{x}","r",encoding='UTF-8')]
			d = [re.findall(find_mov,line) for line in open(f"{x}","r",encoding='UTF-8')]
			aa = [x for x in a if x]
			bb = [x for x in b if x]
			cc = [x for x in c if x]
			dd = [x for x in d if x]
			print(aa,bb,cc,dd)


if __name__ != "__main__":
	execfu = Process(target=this())
	execfu.start()