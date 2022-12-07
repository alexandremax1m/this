import ctypes

from ctypes import *

from os import getlogin

from psutil import win_service_get
from psutil import win_service_iter
from psutil import disk_partitions
from psutil import process_iter
from psutil import Process
from psutil import AccessDenied

from pathlib import Path

from psutil import net_io_counters
from psutil import net_connections
from psutil import net_if_addrs
from psutil import net_if_stats
from requests import get
from requests import Response

from psutil import sensors_battery

winservicesp = c_int * len([x for x in win_service_iter()])
winservicesi = winservicesp(*(tuple([x for x in range(len([x for x in win_service_iter()]))])))

diskpartitionsp = c_int * len([x for x in disk_partitions()])
diskpartitionsi = diskpartitionsp(*(tuple([x for x in range(len([x for x in disk_partitions()]))])))

processesp = c_int * len([x for x in process_iter()])
processesi = processesp(*(tuple([x for x in range(len([x for x in process_iter()]))])))

netconnectionsp = c_int * len([x for x in net_connections()])
netconnectionsi = netconnectionsp(*(tuple([x for x in range(len([x for x in net_connections()]))])))

netifaddrsp = c_int * len([x for x in net_if_addrs()])
netifaddrsi = netifaddrsp(*(tuple([x for x in range(len([x for x in net_if_addrs()]))])))

class BasicData:
    __slots__ = "name","diskprt","netconf","netcons","dosservice"
    def __init__(self,name):
        self.name = str(name)
        self.diskprt,self.netconf,self.netcons,self.dosservice = [],[],[],[]
        __allself__ = (self.diskprt,self.netconf,self.netcons,self.dosservice)
        __allselfi__ = (diskpartitionsi,netifaddrsi,netconnectionsi,winservicesi)
        for i in __allselfi__[0]:
            __allself__[0].append(disk_partitions()[i].device)
        for x in net_if_addrs():
            __allself__[1].append(x)
        for i in __allselfi__[2]:
            __allself__[2].append(net_connections()[i])
        __allself__[3].append([x.display_name() for x in win_service_iter()])
        del __allself__,__allselfi__
        filename = str(input('File Name Sir :: // Just Big :: C >> To Cancel File Writing '))
        if not filename == str('C'):
            open(filename,'a+',encoding='UTF-8').write(f"{self.diskprt},{self.netconf},{self.netcons},{self.dosservice}")
            open(filename,'a+',encoding='UTF-8').close()
        else:
            pass
    def iterdisks(self):
        a = []
        for i in diskpartitionsi:
            a.append([])
            if not a[i]:
                try:
                    a[i] = [x for x in Path(self.diskprt[i]).iterdir()]
                except PermissionError:
                    a[i] = f"Permission error on {self.diskprt[i]}"
        return a
        del a
    def iterdisk(self,disk):
        for i in diskpartitionsi:
            if not self.diskprt[i].startswith(disk) == False:
                try:
                    a = [x for x in Path(self.diskprt[i]).iterdir()]
                except PermissionError:
                    a = f'Permission Error on {disk}'                   
        return a
        del a

class ByteGetReqByteRes():
    __slots__ = "domain"
    def __init__(self,domain):
        self.domain = str(domain)
    def bdata(self):
        return bytes((get(f"{self.domain}").content))


