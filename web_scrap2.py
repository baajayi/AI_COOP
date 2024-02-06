import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))



# Retrieve all of the anchor tags
known_list=[]
url = input("Enter URL: ")
for i in range(count):
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup("a")
    url=tags[position-1].get("href", None)
    print(url)
    known_list.append(tags[position-1].contents[0])


print(known_list[-1])

