#!/usr/bin/env python
import optparse
import socket
import nmap
import pydoc
import geocoder
nm = nmap.PortScanner()
parser = optparse.OptionParser()
parser.add_option("-p","--port",action="store",type="int",dest="port",help="port to be suplied")
parser.add_option("--h0","--host",type="string",action="store",help="the ip for given DNS",dest="host")
#parser.add_option("--scan",type="callback",callback=scan_port(host,port)))
parser.add_option("--msg","--message",type="string",action="store",dest="message",help="payload to be send to the server")
parser.add_option("--ip",type="string",action="store",dest="ip",help=" ip dns lookup")
parser.add_option("--c","--chat",action="store_true",dest="connection",help="if you want to chat")

(options,args) = parser.parse_args()
host = options.host
port = options.port
message = options.message
ip = options.ip
chat = options.connection

def connect(tghost,tgport,payload_msg):
	"""In case you want to connect after you scanned the
		
	target,and send some message dunno payload,get request
	
	or something like that there u go(ps still have to implement some stuff)
	"""
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
	print "ALL PORTS AVBILE FROM 20-80: {}".format(" ".join(str(x) for x in all_ports))
	print "IS THERE ANY INFORMATION ABOUT PORT 80:{}".format(nm[host].has_tcp(80))
	print "INFO FROM PORT 80 ABOUT THE HOST: {}".format(nm[host].tcp(80))
	print "IS PORT 80 PORT OPEN:{}".format(nm[host]['tcp'][80]['state'])
	g = geocoder.google(socket.gethostbyname(host)[0])
	print "the lat and long for the server{}".format(g.latlng)




#pydoc.doc(find_open_port)
#find_open_port(host)
#connect(host,port,message)
