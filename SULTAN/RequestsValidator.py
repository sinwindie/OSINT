import requests

url = "INSERT URL TO USER PROFILE HERE"
r = requests.get(url)
html = r.text
notfound = (html.find("INSERT ERROR TEXT HERE"))
            
#If profile with username exists
if notfound == -1:
    print url           # Prints url to profile
#If profile with username does not exist
else:
    print html          # Prints HTML to search for error code
