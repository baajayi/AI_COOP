import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
s=0
url = "http://py4e-data.dr-chuck.net/comments_1958298.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
for tag in tags:
    s+=int(tag.contents[0])
print(s)