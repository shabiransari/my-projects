
from bs4 import BeautifulSoup
import requests
url = 'http://www.winequality.com'
r = requests.get(url)
html_doc = r.text
print(html_doc)
soup = BeautifulSoup(html_doc)
print(soup.prtify)
print(soup.title)
tags = soup.find_all('a')
for link in tags:
	print(link.get('bref'))
url1 = 'http://www.analyticsindiamag.com'
r = requests.get(url1)
html_doc = r.text
print(html_doc)
soup = BeautifulSoup(html_doc)
print(soup.prtify)



