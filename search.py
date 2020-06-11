import csv 
import os
import webbrowser
import requests
from tkinter import*
import urllib.parse as urlparse
from urllib.parse import parse_qs
url = 'https://drsureshmondal.in/search.py?q=silence&as_sitesearch=drsureshmondal.in'
parsed = urlparse.urlparse(url)
q= parse_qs(parsed.query)['q']
as_sitesearch = parse_qs(parsed.query)['as_sitesearch']
    # url of rss feed 
url1 = 'https://infiniteamp.blogspot.com/feeds/posts/default'
    
   # creating HTTP response object from given url 
resp = requests.get(url1, params= {'q':q}) 

    

    # saving the xml file 

with open('https://drsureshmondal.in/topnewsfeed.xml', 'wb') as f: 

    f.write(resp.content) 
        
file = ('https://drsureshmondal.in/topnewsfeed.xml')
#brw = 'am start --user 0 -a android.intent.action.VIEW -n com.example.yourappname/.MainActivity  -d %s'
#cmd= brw % file


webbrowser.open(file)

  

 
        

          
