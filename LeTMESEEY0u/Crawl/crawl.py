import requests
import re
import random
import datetime
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen

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
        print(title)
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
