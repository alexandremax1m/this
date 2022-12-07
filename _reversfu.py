import os, re, subprocess
import ctypes, multiprocessing

from multiprocessing import Process

find_has = re.compile(r"HAS.{0,100}")

def findhas():
	
	for x in os.listdir():
		if x.endswith('.o'):
			a = subprocess.run(["objdump","-f",f"{x}"],text = True, capture_output=True)
			b = re.findall(find_has,a.stdout)
			with open(f"{x[0:5]}.txt","a+",encoding='UTF-8') as file:
				for x in b:
					file.write(x)
					file.close()

if __name__ != "__main__":
	execthis = Process(target=findhas())
	execthis.start()