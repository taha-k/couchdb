import requests
import json

for index in range(1,1561):
	udid = requests.get("http://127.0.0.1:5984/_uuids")
	udid = udid.json()
	udid = udid['uuids'][0]

	json_data=open("books-json/book" + str(index) + ".json").read()

	response = requests.put("http://127.0.0.1:5984/bk", str(json_data))
	print index
