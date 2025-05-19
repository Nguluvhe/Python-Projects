import requests
import json

# answers api key response = requests.get("https://api.stackexchange.com//2.3/answers?order=desc&sort=activity&site=stackoverflow")

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    print(data['title'])