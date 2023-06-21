import requests
import json

response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

# print(f"Response json {response.json()['items']}")

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'], data['link'])
        print('-----------------')
    else:
        print('skpped')
        print('-----------------')
