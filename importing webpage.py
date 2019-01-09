from urllib.request import urlopen, Request 
import pandas as pd 
url = 'http://nullshell.com'
contents = urlopen(url)
read = contents.readlines()
print(read)
import requests
url = 'http://www.wikipedia.org/'
r = requests.get(url)
text = r.text
print(text)