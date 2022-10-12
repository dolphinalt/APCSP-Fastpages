import requests

url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

querystring = {"aggregateHours":"24","location":"Washington,DC,USA","contentType":"csv","unitGroup":"us","shortColumnNames":"0"}

headers = {
	"X-RapidAPI-Key": "eb0bbc6cc0msh085b254f1761bc2p154cf4jsne59a8dbdbaa0",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)