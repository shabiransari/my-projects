#JSON(javascript object notation) realtime server_to_browser communication
#Loading json in python
import json
with open('E:\csvdhf5xlsxurlallfiles/snakes.json', 'r') as json_file:
	json_data = json.load(json_file)
	print(type(json_data))
	for key, value in json_data.items():
		print(str(key)+':'+str(value))
#connecting to an API in python
import requests
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
	print(str(key)+':'+str(value))
url1 = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'
r = requests.get(url1)
json_data = r.json()
for k in json_data.keys():
	print(k+':', json_data[k])
url2='http://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&enintro=&titles=pizza'
r = requests.get(url2)
json_data = r.json()
pizza_exract = json_data['query']
print(pizza_exract)
import tweepy, json 






