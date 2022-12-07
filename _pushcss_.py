import re

from os import getcwd
from pathlib import Path

class CSSFile:
	__slots__ = "filename","htmlfilename"
	def __init__(self,filename):
		self.filename = f"{filename}"
		a = [x for x in Path(getcwd()).iterdir() if str(x).endswith(f"{self.filename}")]
		if not a:
			open(f"{self.filename}",'a+',encoding='UTF-8').close()
		del a
	def write(self):
		pass
		
		