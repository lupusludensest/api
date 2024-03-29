import requests

payload = {
        'key1': 'value1',
        'key2': 'value2'
}
r = requests.post('https://httpbin.org/post/lol', data=payload)

print(r.content)  # raw response as bytes
print(r.text) # decoded response
print(r.url) # url of the response

if r.status_code == 200:
    print(f"PASS_STATUS = {r.status_code}")
else:
    print(f'\nFAIL_STATUS ="{r.status_code}"')
