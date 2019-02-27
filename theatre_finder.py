import urllib.request
import urllib.parse
import json
key = "aL3w20eL2TddFXPpYFUOTbGaOXfXe6Gt"
address = input("What's your location? ")
address = address.replace(" ","%20")


url = 'http://www.mapquestapi.com/search/v2/radius?key=' + key + '&maxMatches=500&radius=20.0&units=m&origin=' + address
f = urllib.request.urlopen(url)
response_object = json.loads(f.read().decode('utf-8'))
search_results = response_object['searchResults']
lst = []
for result in search_results:
	if result['fields']['group_sic_code'].startswith('78'):
		lst.append(result['name'] + ", " + result['fields']['address'] + ", " + result['fields']['city'] + ", " + result['fields']['state'] + " - " + result['fields']['postal_code'])

lst.sort(key = lambda x: x.split(",")[1])
for lst_element in lst:
	print(lst_element)