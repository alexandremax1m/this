from os import getcwd
from pathlib import Path

from _pushcss_ import *
from _pushcss_ import CSSFile 

if __name__ != "__main__":
	print([x for x in Path(getcwd()).iterdir() if str(x).endswith('.html')])
	print(open(f"{str(input('Choose Your File To Read Sir :: '))}",'r',encoding='UTF-8').read())
	while True:
		if not str(input('Do You Want To Read Or Write Sir :: read | write ')) == 'write':
			print(open(f"{str(input('Choose Your File To Read Sir :: '))}",'r',encoding='UTF-8').read())
		else:
			break
		
		
	