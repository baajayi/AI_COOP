import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags=soup("a")

# Retrieve all of the anchor tags
known_list=[]
for i in range(count):
    known_list.append(tags[position].contents[0])


print(known_list)

