from os import system
import requests
import bs4 , time ,sys
import tor 
from selenium import webdriver  
from pathlib import Path


def get_html (url):
    r = requests.get (url)
    data = r.text
    print (data )
    return data 

def get_html_tor (url):
    return tor.get_html_tor  (url )
     

def get_json (url):
    r = requests.get (url)
    data = r.json ()   
    return data 

def save_txt_file (file_name ,data):
    open(file_name, 'a+' , encoding='utf-8').write( data )
 
def get_cli_arguments ():
    l = sys.argv 
    l.pop (0 )
    return l

def read_file (file_name ):
    return open( file_name).read().splitlines()


def bs4_form_string (txt):
    bs4_obj = bs4.BeautifulSoup ( txt  , features="lxml")
    return  bs4_obj 

def bs4_form_file (file):   
    f = read_file  (file )
    bs4_obj = bs4.BeautifulSoup ( f    , features="lxml")
    return  bs4_obj 

def bs4_form_url (url):
    l = get_html (url)
    bs4_obj = bs4.BeautifulSoup ( l   , features="lxml")
    return  bs4_obj 


def bs4_find (link  ,selector, type ):
    match type :
        case "url":            
            l = get_html (link )
            bs4_obj = bs4.BeautifulSoup (l , features="lxml")
        case "string":
            bs4_obj = bs4.BeautifulSoup (link  , features="lxml")
        case "file":
            l = read_file (link )
            bs4_obj = bs4.BeautifulSoup (l.join  ('') , features="lxml"  )
    return  bs4_obj.select (selector )

def bs4_find_tor (p ,selector, type ):
    match type :
        case "url":            
            l = tor.get_html_tor (p)
            bs4_obj = bs4.BeautifulSoup (l , features="lxml")
        case "string":
            bs4_obj = bs4.BeautifulSoup (p , features="lxml")
        case "file":
            l = read_file (p)
            bs4_obj = bs4.BeautifulSoup (l.join  ('') , features="lxml"  )
    return  bs4_obj.select (selector )


def extract_html_from_list_of_pages (url_file ,selector ,  sleep_):
    lines = read_file (url_file )
    for item in lines :
        time.sleep (sleep_   )
        elem = bs4_find(item ,selector , "url")
        print ( elem )
        save_txt_file  ( "./mydata" , str(elem)+"\n")
        print ( "done scraping with ==>> " + item  )


def extract_html_from_list_of_pages_tor (url_file ,selector ,  sleep_):
    lines = read_file (url_file )
    for item in lines :
        time.sleep (sleep_   )
        elem = bs4_find_tor(item ,selector , "url")
        print ( elem )
        save_txt_file  ( "./mydata" , str(elem)+"\n")
        print ( "done scraping with ==>> " + item  )
 



def selenium (cmd_list):
# the list should have 4 params [url,css_selector,sleeping_time,javascript_to_execute,result_saving_file]
# list exemple 
#  [["http://www.youtube.com" ,
#      "*" ,
#      3,
#     "document.body.innerHTML = ''",
#      "./selenium_result/output.txt"]
#      ,
#      ["http://www.kooora.com" ,
#       "*" ,
#       0,
#       "",
#      "./selenium_result/output.txt"],
#     ]
    driver=webdriver.Chrome(r"../browsers\chromedriver.exe")  
    driver.maximize_window()  
    for x in cmd_list : 
        url = str(x[0])
        css_selector = str(x[1])
        sleep_timer = int(x[2])
        javascript = str(x[3])
        saving_file = str(x[4])

        print (url  , css_selector , sleep_timer ,javascript , saving_file )
        driver .get ( url )
        # print (f)
        print (x[3])
        if  javascript :
            driver.execute_script (javascript)

        f = driver.find_element_by_css_selector(css_selector).text
        with open(saving_file, 'a+' , encoding="utf-8") as l:
            l.write(str(f) )
            l.close ()
    
        time.sleep (sleep_timer)
         


def publipostage ( args_list , module_string): 
    return ( module_string.format ( *args_list))

def publipostage_save ( args_list , module_string,file_name): 
     save_txt_file (file_name , module_string.format ( *args_list))