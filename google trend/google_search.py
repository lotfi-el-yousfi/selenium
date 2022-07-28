import requests


keyword ="pdf"
url="https://www.google.com/search?q=" + keyword

r= requests.get( url )
print ( r.text )