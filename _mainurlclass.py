import ftplib, telnetlib, smtplib
import threading, multiprocessing
import socket, ssl, ipaddress, requests
import json, pyfiglet, re

from requests import get

class URL:
    
    url: str
    
    def __init__(self, url):
        
        self.url = url
         
    def index_to_file(cls):
        response = get(cls.url)
        with open(f"{cls.url[12: -4]}.txt", "x",encoding='utf-8') as f:
            f.write(f"{response.text}")
       
    def look_for(cls, word):
        cls.word = str(word)
        with open(f"{cls.url[12: -4]}.txt",  "r",encoding='utf-8') as file:
            content = file.read()
            if word in content:
                return True
            else:
                return False   
   
    def toip(cls):
        return socket.gethostbyname(f"{cls.url[12:]}")
   
    def query(cls, query):
        query = query
        return get(f"{cls.url}{query}")

    def random_arbitrary_query(cls):
        random_query = [r"/admin","/login","/users"]
        for x in random_query:
            valid_request = get(f"{cls.url}{x}")
            if valid_request.status_code == 200:
                print(f"{cls.url}{x}  is TRUE")
            else:
                print(f"{cls.url}{x}  is FALSE")

    def portscan(cls, start, end):
        cls.start = int(start)
        cls.end = int(end)
        ipadd = socket.gethostbyname(f"{cls.url[12:]}")
        ports = [ x for x in range(cls.start,cls.end) ]
        for port in ports:
            print(f"Trying {ipadd}:{port}")
            my_socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            my_socketobj_method = my_socket_obj.connect_ex((ipadd,port))
            if my_socketobj_method == 0:
                print(f"{port} open on {ipadd}")
            else:
                print(f"Port {port} on {ipadd} not open")
    
    def data_classifier(cls, arg):
        cls.arg = str(arg)
        if arg == "img":
            pattern_5 = re.compile(r"<img.{0,1000}$")
            tef = [re.findall(pattern_5,line) 
                              for line in open(f"{cls.url[12: -4]}.txt", "r",encoding='utf-8')]
            tff = [x for x in tef if x]
            for x in tff:
                print("\n",x)
        elif arg =="js":
            pattern = re.compile(r"<script.{0,1000}</script>$")
            a = [re.findall(pattern,line) 
                            for line in open('flashscore.txt','r',encoding='UTF-8')]
            b = [x for x in a if x] 
            for x in b:
                print("\n",x)
        else:
            pass
                
    def get_headers(cls):
        req = requests.get(cls.url)
        print(str(req.headers))
    
    def ipinfo(cls):
        ipadd = socket.gethostbyname(f"{cls.url[12:]}")
        req_two = requests.get("https://ipinfo.io/"+str(ipadd)+"/json")
        print(req_two.text)
            
    def help(cls):
        ascii_banner = pyfiglet.figlet_format("URL CLASS")
        print(ascii_banner)

                


