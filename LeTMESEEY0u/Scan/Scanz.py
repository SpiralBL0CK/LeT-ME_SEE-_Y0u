def connect(tghost, tgport, payload_msg):
    import socket
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        fd.connect((tghost, tgport))
        b = fd.send(payload_msg)
        print ("connected to port{}").format(port)
        if "220 hostname FTP server (Version wu-2.4.2-academ[BETA-18](1) Mon Jan 15 15:02:27 JST 1999) ready" in b:
            print ("found vulnerable ftp")
        elif "220 hostname FTP server (Version wu-2.5.0(1) Tue Jun 15 12:43:57 MST 1999) ready" in b:
            print ("found voulnerable ftp")
        elif "220 ProFTPD 1.2.4 Server (hostname) [hostname]" in b:
            print ("found vulnerable ftp")
        else:
            print ("we couldn't find anything souspicious about the server")
        fd.close()

    except socket.error:
        print ("cant connect to host,port closed{}").format(port)

def find_open_port(host):
    """The name of this function is pretty explicit

           with what is does.Also go check the documentation out.

        It's free id doesn't cost anything.
        https://pypi.python.org/pypi/python-nmap
    """
    import socket
    import nmap
    import geocoder
    nm = nmap.PortScanner()
    name = socket.gethostbyaddr(host)[0]
    ip_from_name = socket.gethostbyname(ip)
    print( ip_from_name)
    print ("INFO ABOUT THE SPECIFIC REVERSE DNS LOOKUP: {}").format(name)
    scanned = nm.scan(host, '20-80')
    all_hosts = nm.all_hosts()
    all_ports = nm[host].all_tcp()
    print ("ALL PORTS AVBILE FROM 20-443: {}").format(" ".join(str(x) for x in all_ports))
    print ("IS THERE ANY INFORMATION ABOUT PORT 80:{}").format(nm[host].has_tcp(80))
    print ("INFO FROM PORT 80 ABOUT THE HOST: {}").format(nm[host].tcp(80))
    print ("IS PORT 80 PORT OPEN:{}").format(nm[host]['tcp'][80]['state'])
    g = geocoder.google(socket.gethostbyname(host)[0])
    print(g.latlng)
