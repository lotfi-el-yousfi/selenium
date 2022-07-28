from time import sleep
import functions
import os 
import sys 

# python web_data_extractor.py  python_w3shools_ref_links   "title"  4 false


# os.system('clear')
print  (''' 
                                   
                __                                                     __             __      __  _____ 
 _      _____  / /_     ___________________ _____  ____  ___  _____   / /_  __  __   / ____  / /_/ __(_)
| | /| / / _ \/ __ \   / ___/ ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/  / __ \/ / / /  / / __ \/ __/ /_/ / 
| |/ |/ /  __/ /_/ /  (__  / /__/ /  / /_/ / /_/ / /_/ /  __/ /     / /_/ / /_/ /  / / /_/ / /_/ __/ /  
|__/|__/\___/_.___/  /____/\___/_/   \__,_/ .___/ .___/\___/_/     /_.___/\__, /  /_/\____/\__/_/ /_/   
                                         /_/   /_/                       /____/                         
                                   
''')

 


params = functions.get_cli_arguments ( )

file_name = params[0] 
selector  = params[1]
sleep_    = int (params[2])

if params[3] == "true" :
    functions.extract_html_from_list_of_pages_tor ( file_name  , selector  , sleep_ )
else :
    functions.extract_html_from_list_of_pages ( file_name  , selector  , sleep_ )
