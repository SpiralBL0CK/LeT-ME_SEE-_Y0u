# LeT-ME_SEE-_Y0u
basic skeleton for a python port scanner and a webcrawler included.

# Usage: LeT-ME_SEE-_Y0u.py [options]
Options:

  -h, --help                show this help message and exit
  
  -p PORT, --port=PORT      port to be suplied
  
  --h0=HOST, --host=HOST    the ip for given DNS             
  
  --msg=MESSAGE, --message= MESSAGE payload to be send to the server   
  
  --ip=IP                   ip for dns lookup
  
  --c, --chat               answer if you want to chat

  --s, --scrap              scrap a website to extract data from a specific webiste(* hardly trying to learn how to use it,so will take some time to be implemented)(also under construction as usual)
  
  --b, --brute-force        decide if you want to bruteforce some ftp
  
# To run the basic crawler(no functionality yet,but it works can run with no errors):

scrapy crawl LetMESEEYOu -a host=""

Before executing the script you have to go to the root directory of the project and than execute the command above.

yOu should check out the docs if you want and it will be easyer for you see understand what i mean.
https://doc.scrapy.org/en/latest/topics/commands.html

# Requirements:
nmap:sudo apt-get install nmap

geocoder: sudo apt-get install geocoder

python-nmap : sudo pip install python-nmap

scrapy: pip install Scrapy / conda install -c conda-forge scrapy


# !Please note that all i do is for fun and to learn,so dont yell to me if i did s0mething wr0ng.
Also This is under C0nstruction,i'll add some more features.
