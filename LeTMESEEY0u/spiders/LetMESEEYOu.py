#!/usr/bin/env python
import optparse
import socket
import nmap
import scrapy
import pydoc
import geocoder
import ftplib
import smtplib
import smpt


class MySpider(scrapy.Spider):
    """Crawler Class
    """
    
    name = "LetMESEEYOu"
    def __init__(self,host='', *args,**kwargs):
        super(MySpider,self).__init__(*args,**kwargs)
        self.host = host
        allowed_host = [self.host]
        start_url = [self.host]
        
    def request(self,host,param):
        yield scrapy.Request(self.host.append(self.param))
        
def scan(host,argz):
    """This will be the callback of implementation of scapy functionalities
        
        Also this function wont do more than scapping your data from
        
        a given host searching by your given params(a.k.a selectors)
    
    """

"""
!NOTE:under construction still figuring out how to do stuff,READING A LOT ABOUT CRAWLERS,AND IN THE SAME TIME LEARNING PYTHON SO GIVE ME A BREAK IM 16 ONLY.
ALSO NOTE I STILL TRY TO FIGURE OUT HOW TO ARENGE THE SCRIPT SO YEAH, IN THE FUTURE MAYBE THERE WILL BE SOME GUI AND THE SCRIPT WILL BE FULLY DONE.Until than stay tuned for more 
if u want.Thake it easy guyz.
"""

nm = nmap.PortScanner()
parser = optparse.OptionParser()
parser.add_option("-p","--port",action="store",type="int",dest="port",help="port to be suplied")
parser.add_option("--h0","--host",type="string",action="store",help="the ip for given DNS",dest="host")
#parser.add_option("--scan",type="callback",callback=scan_port(host,port)))
parser.add_option("--msg","--message",type="string",action="store",dest="message",help="payload to be send to the server")
parser.add_option("--ip",type="string",action="store",dest="ip",help=" ip dns lookup")
parser.add_option("--argz",type="string",action="store",dest="argz",help="criteria of how you want to scrap the data from the given website")
parser.add_option("--c","--chat",action="store_true",dest="connection",help="if you want to chat")
#parser.add_option("--s","--scrap",type="callback",callack=scan(host,argz))
parser.app_option("--b","--brute-force",action="store_true",dest="brute_force")
(options,args) = parser.parse_args()
host = options.host
port = options.port
message = options.message
ip = options.ip
chat = options.connection
argz = options.argz
brute_force = options.brute_force

def brute(host):
#mainly done has to be bounded with the option	
    ftp = ftplib.FTP(host)
    with open("list.txt","r") as f:
        data = [x.strip().split(' ') for x in f.readlines()]
        
    for username,password in data:
        ftp.login(username,password)

def connect(tghost,tgport,payload_msg):
	fd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		fd.connect((tghost,tgport))
		fd.send(payload_msg)
		print "connected to port{}".format(port)
		fd.close()

	except socket.error:
		print "cant connect to host,port closed{}".format(port)


def find_open_port(host):
	"""The name of this function is pretty explicit

	   	with what is does.Also go check the documentation out.

		It's free id doesn't cost anything.
		https://pypi.python.org/pypi/python-nmap
	"""
	name = socket.gethostbyaddr(host)[0]
	ip_from_name = socket.gethostbyname(ip)
	print ip_from_name
	print "INFO ABOUT THE SPECIFIC REVERSE DNS LOOKUP: {}".format(name)
	scanned = nm.scan(host,'20-80')
	all_hosts = nm.all_hosts()
	all_ports = nm[host].all_tcp()
	print "ALL PORTS AVBILE FROM 20-443: {}".format(" ".join(str(x) for x in all_ports))
	print "IS THERE ANY INFORMATION ABOUT PORT 80:{}".format(nm[host].has_tcp(80))
	print "INFO FROM PORT 80 ABOUT THE HOST: {}".format(nm[host].tcp(80))
	print "IS PORT 80 PORT OPEN:{}".format(nm[host]['tcp'][80]['state'])
	g = geocoder.google(socket.gethostbyname(host)[0])
	print g.latlng


#pydoc.doc(find_open_port)
#find_open_port(host)
#connect(host,port,message)
