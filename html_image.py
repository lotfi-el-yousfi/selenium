import imgkit
import requests 
import json

for i in range (200):
    image  = requests.get ("https://dog.ceo/api/breeds/image/random")
    data_str =     image.json ( )   
    image_url =  (data_str["message"]) 


    imagge_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title></title>
    </head>
    <body>
        <center>
        <h1>
        this is my dog
        </h1>

            <img src=""" + image_url + """ ">
            </center> 
    </body>
    </html>

    """
    l  = r".\images\{}.jpg"
    l= l.format (i)
    imgkit.from_string ( imagge_html   , l )
