import requests

payload = {'key1': 'value1', 'key2' : ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)

print('URL: ', r.url)
print('ENCODING: ', r.encoding)
print('STATUS_CODE: ',r.status_code)
print('HEADERS: ', r.headers)
print('TEXT', r.text)
print('CONTENT: ', r.content)
print('JSON', r.json)




