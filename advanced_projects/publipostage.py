import sys
import functions
from inspect import getmembers, isfunction


functions.publipostage (["google" , "youtube"] , "https://www.{0}.com" )

# description   = (
# '''
# you should enter three arguments 

#     1- array contains all words to replace in side text  
#     2- text to manipulate  
#     3- file path to save the result  

#     exemple  : ['good ' ,'bad'] ,  {0} is better 
#     than {1} but you know 
#     not all{0} is {0}
#     hhhh
# ''')

# # args = functions.get_cli_arguments ()
# # functions.publipostage_save (*args)


# current_module = sys.modules[__name__]
# list  = (getmembers(current_module , isfunction))
# functions_list =[]
# for item in list :
#     functions_list.append (item [0])

# print  (functions_list)


# # print the description 

# # display all function with a brief description and a referenciation number 
# script_description = ''
# print  (script_description )
# function_choise  = (  int (input  ( ))  )

# # input the function number choosen by the user 
# # display description of the function 
# function_description   =""
# print ( function_description )

# # input the list of arguemnts  args
# functions_args  = functions.get_cli_arguments ( )
# # execute the function 
# result = functions_list[function_choise]( *functions_args)
# # display result
# print  (result )  