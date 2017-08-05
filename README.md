# LeT-ME_SEE-_Y0u
basic skelet for the construction of a python port scanner and a webcrawler included.

# Usage: LeT-ME_SEE-_Y0u.py [options]
Options:

  -h, --help                show this help message and exit
  
  -p PORT, --port=PORT      port to be suplied
  
  --h0=HOST, --host=HOST    the ip for given DNS             
  
  --msg=MESSAGE, --message= MESSAGE payload to be send to the server   
  
  --ip=IP                   ip for dns lookup
  
  --c, --chat               answer if you want to chat

  --s, --scrap              scrap a website to extract data from a specific webiste(* hardly trying to learn how to use it,so will take some time to be implemented)(also under construction as usual)
  
# To run the basic crawler(no functionality yet,but it works to be run with no errors):

scrapy crawl LetMESEEYOu -a host="http://www.google.ro"

Before executing the script you have to go to the root directory of the project and than execute the command above.

# Requirements:
nmap:sudo apt-get install nmap

geocoder: sudo apt-get install geocoder

python-nmap : sudo pip install python-nmap

scrapy: pip install Scrapy / conda install -c conda-forge scrapy


# !Please note that all i do is for fun and to learn,so dont yell to me if i did s0mething wr0ng.
Also This is under C0nstruction,i'll add some more features.
