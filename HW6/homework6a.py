from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

numbers =[]
for tag in tags:
    num = int((tag.contents[0]))
    numbers.append(num)

total = 0
for x in numbers:
	total = total + x

print (total)
return total

