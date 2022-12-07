from pathlib import Path
from psutil import win_service_iter
from psutil import win_service_get

def test1():
	for x in win_service_iter():
		print(f"{x.name()} :: {x.binpath()}")

def test2():
	a,b,perm = [x for x in Path('C:\\Windows').iterdir() if x.is_dir()],[],[]
	for x in range(len(a)):
		b.append([])
		if not b[x]:
			try:
				b[x] = [x for x in a[x].iterdir()]
			except PermissionError:
				perm.append(a[x])
	print(a,b,perm)
	del a,b,perm