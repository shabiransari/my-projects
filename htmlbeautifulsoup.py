import requests
from bs4 import BeautifulSoup
url = 'http://www.python.org/~guido/'
r = requests.get(url)
url = 'http://python.org/~guido/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.title)
a_tags = soup.find_all('a')
for link in a_tags:
	print(link.get('href'))
import json
with open('snakes.json', 'r') as json_file:
	json_data = json.load(json_file)
print(type(json_data))




