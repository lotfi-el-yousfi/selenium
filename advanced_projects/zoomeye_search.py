import functions 

data= functions.get_html_tor ( "https://www.zoomeye.org/searchResult?q=goautodial%20%2bcountry:%22US%22&t=all")
 

open("./zoomeye.txt", 'a+' ,encoding= "utf-8" ).write( data )