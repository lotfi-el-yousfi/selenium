from time import sleep
import functions
import os
import sys
import re 
 
 
# python google_email_extractor.py  python_w3shools_ref_links   "title"  4 false


# os.system('clear')
print(''' 
                                   
 ██████   ██████   ██████   ██████  ██      ███████     ███████ ███    ███  █████  ██ ██      
██       ██    ██ ██    ██ ██       ██      ██          ██      ████  ████ ██   ██ ██ ██      
██   ███ ██    ██ ██    ██ ██   ███ ██      █████       █████   ██ ████ ██ ███████ ██ ██      
██    ██ ██    ██ ██    ██ ██    ██ ██      ██          ██      ██  ██  ██ ██   ██ ██ ██      
 ██████   ██████   ██████   ██████  ███████ ███████     ███████ ██      ██ ██   ██ ██ ███████ 
                                                                                              
                                                                                              
███████ ██   ██ ████████ ██████   █████   ██████ ████████  ██████  ██████                 
██       ██ ██     ██    ██   ██ ██   ██ ██         ██    ██    ██ ██   ██                
█████     ███      ██    ██████  ███████ ██         ██    ██    ██ ██████                 
██       ██ ██     ██    ██   ██ ██   ██ ██         ██    ██    ██ ██   ██                
███████ ██   ██    ██    ██   ██ ██   ██  ██████    ██     ██████  ██   ██                
                                                                                              
                                                                                              
██████  ██    ██     ██       ██████  ████████ ███████ ██                                     
██   ██  ██  ██      ██      ██    ██    ██    ██      ██                                     
██████    ████       ██      ██    ██    ██    █████   ██                                     
██   ██    ██        ██      ██    ██    ██    ██      ██                                     
██████     ██        ███████  ██████     ██    ██      ██                                     
                                                                                              
                                                                                              
                                   
''')


# google_dork = 'intext:"gmail.com" site:linkedin.com/in shubham'
# saving_file = "links.txt"
# email_pattern = '''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''


# def google_dork_search():
#     return functions.bs4_find("https://www.google.com/search?q="+google_dork, "a","url")


# print(google_dork_search())

functions.selenium ( )

# matchs = re.findall( email_pattern, str(google_dork_search())  )
# print(matchs)
