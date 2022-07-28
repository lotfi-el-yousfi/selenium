import requests
import os
import sys


def check_url(url):
    r = requests.get(url)
    if "password" not in r.url:
        open('results.txt', 'a+').write(r.url+'\n')



try:
    # os.system('clear')
    sites = open(sys.argv[1]).read().splitlines()
    for x in sites:
        check_url(x)
          
    print (' Done saved in results.txt')
except IndexError:
    exit("error")
except:
    exit("error")