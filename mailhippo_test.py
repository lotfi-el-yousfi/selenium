import  time 
import re
from selenium import webdriver  



email  ="lotfi@yahoo.com"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver=webdriver.Chrome(r"browsers\chromedriver.exe" , chrome_options=chrome_options)  
driver.maximize_window()  
driver.get("https://tools.emailhippo.com/")


input  = driver.find_element_by_id ("input-email-address")
input.send_keys (email)

print  ( driver.find_element_by_css_selector(".input-group-append>button") )
driver.find_element_by_css_selector(".input-group-append>button").click()

