from _mainurlclass import *
from _mainurlclass import URL

my_urls_list = []

while True:
    print("Enter URL to init, type stop to start")
    a = str(input())
    my_urls_list.append(a)
    if a == "stop":
        my_urls_list.remove(a)
        break

_sz = len(my_urls_list)

for x in range(_sz):
    url_x = URL(my_urls_list[x])
    ip_x = url_x.ipinfo()
    headers_x = url_x.get_headers()
    print(ip_x)
    print(headers_x)
    url_x.index_to_file()




