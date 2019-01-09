from urllib.request import urlopen, Requests
url = 'http://www.datacamp.com/teach/documentation'
request = Request(url)
response = urlopen(request)
print(type(request))
response.close()
html = response.read()
response.close() 
print(html) 
#BeautifulSoup parse and extract structured data from HTML
from bs4 import BeautifulSoup
url = 'http://www.crummy.com/software/BeautifulSoup'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.pritify())




