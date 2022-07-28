import requests
import functions
 
countries_list   =[ 
"united_states" , 
"australia" , 
"canada"  , 
"united_kingdom" , 
"germany" , 
"switzerland" , 
"brazil" , 
"new zealand" , 
"italy"  
] 
url = "https://trends.google.com/trends/hottrends/visualize/internal/data"
r = requests.get (url)
data = r.json () 
 
# print all list 
for i in countries_list: 
    print ( data [i])

# save kewrods as cmd command to statr it in chrome 
def loop_write(array_name):
    for x in array_name:
        open("./google_trend_list_by_country/google_links.txt", 'a+').write( "start chrome.exe https://www.google.com/search?q=" + x +"&&" )
        open("./google_trend_list_by_country/google_links.txt", 'a+').write( "start chrome.exe https://www.google.com/search?q=" + x +"&tbm=isch&&" )


# save each list to a file 
for item in countries_list:
    open("./google_trend_list_by_country/"+item+".txt", 'a+').write(str(data[item])) 
    # add links to google links bat file for autolaunching  
    loop_write (data[item])

print('done !')
 
