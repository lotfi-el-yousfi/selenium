import requests
import time
from pyquery import PyQuery as pq

from stem import Signal
from stem.control import Controller


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session
 
# signal TOR for a new connection 
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="password")
        controller.signal(Signal.NEWNYM)
        time.sleep(6)


def get_html  (url):    
    session = get_tor_session()
    renew_connection ()
    return   session.get(url).text 

def write_to_file (file_name, data ):
    f = open(file_name, "w")
    f.write(data )
    f.close()

# print (get_html("http://httpbin.org/ip")) 
html  = pq (get_html("https://www.datacamp.com"))

write_to_file ("data.html", get_html  ( 
"https://w.cima4u.ws/v85/"
) )