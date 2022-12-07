from os import getcwd
from pathlib import Path

class HTMLFile:
	__slots__ = "filename","cssfilename"
	def __init__(self,filename):
		self.filename = f"{(str(filename))}"
		a = [x for x in Path(getcwd()).iterdir() if str(x).endswith(f"{self.filename}")]
		if not a:
			open(f"{self.filename}",'a+',encoding='UTF-8').close()
		del a
	def count_lines(self):
		print(len([x for x in open(f"{self.filename}",'r',encoding='UTF-8').readlines()]))
		open(f"{self.filename}",'a+',encoding='UTF-8').close()
	def writet(self,title):
		t, tt = f"<title>",f"</title>"
		open(f"{self.filename}",'a+',encoding='UTF-8').write(f"{t}{title}{tt}")
		open(f"{self.filename}",'a+',encoding='UTF-8').close()
	def writebd(self):
		bd, bdbd = f"<body>",f"</body>"
		open(f"{self.filename}",'a+',encoding='UTF-8').write(f"{bd}\n{bdbd}")
		open(f"{self.filename}",'a+',encoding='UTF-8').close()
	def writeh(self,header):
		h, hh = f"<h1>",f"</h1>"
		open(f"{self.filename}",'a+',encoding='UTF-8').write(f"{h}{header}{hh}\n")
		open(f"{self.filename}",'a+',encoding='UTF-8').close()
	def writep(self,ppp):
		p, pp = f"<p>",f"</p>"
		open(f"{self.filename}",'a+',encoding='UTF-8').write(f"{p}{ppp}{pp}\n")
		open(f"{self.filename}",'a+',encoding='UTF-8').close()
	def writeahr(self,link,look):
		a, aa, linkk, look = f"<a",f"</a>",f"'{link}'",f"{look}"
		open(f"{self.filename}",'a+',encoding='UTF-8').write(f"{a} href={linkk}>{look}{aa}\n")
		open(f"{self.filename}",'a+',encoding='UTF-8').close()
	def addimg(self,img,altt,w,h):
		i,ii,iii,iiii,iiiii = f"<img ",f"src={img} ",f"alt={altt} ",f"width={w} ",f"height={h}>"
		open(f"{self.filename}",'a+',encoding='UTF-8').write(f"{i}{ii}{iii}{iiii}{iiiii}\n")
		open(f"{self.filename}",'a+',encoding='UTF-8').close()
	def makecssfile(self,cssfilename):
		self.cssfilename = f"{(str(cssfilename))}"
		open(f"{self.cssfilename}",'a+',encoding='UTF-8').close()
	def cssedit(self,tagged):
		pass

class Website:
	__slots__ = "webpages","style","database"
	def __init__(self,webpages):
		self.webpages = webpages
		if not type(self.webpages) == list:
			self.webpages = []
			if type(webpages) == str:
				self.webpages.append(webpages)
			elif type(webpages) == tuple or type(webpages) == list:
				self.webpages = list(webpages)
		a = [x for x in Path(getcwd()).iterdir()]
		b = [str(c) for c in a if str(c).endswith(tuple([f"{x}" for x in self.webpages]))]
		if not b:
			for x in self.webpages:
				open(f"{x}",'a+',encoding='UTF-8').close()
		del a,b
	def addfile(self,filename):
		open(f"{filename}",'a+',encoding = 'UTF-8').close()
	def editfile(self,filename):
		pass		
