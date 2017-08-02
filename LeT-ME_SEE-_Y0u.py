#!/usr/bin/env python
import optparse
import socket
import nmap
nm = nmap.PortScanner()
parser = optparse.OptionParser()
parser.add_option("-p","--port",type="int",dest="port")
parser.add_option("--h0","--host",type="string",dest="host")
#parser.add_option("--scan",type="callback",callback=scan_port(host,port))
(options,args) = parser.parse_args()
host = options.host
port = options.port
'''
def connect(tghost,tgport):
	fd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		fd.connect((tghost,tgport))
		print "connected to port{}".format(port)
		fd.close()

	except socket.error:
		print "cant connect to host,port closed{}".format(port)
'''

def scan_port(host):
	name = socket.gethostbyaddr(host)[0]
	scanned = nm.scan(host,'20-43')
	all_hosts = nm.all_hosts()
	print all_hosts
	print nm[host]['tcp'].keys()
#scan_port(host)
#connect(host,port)
