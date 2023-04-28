import requests

r = requests.get('https://httpbin.org/basic-auth/corey/_testing', auth=('corey', '_testing'))

print(r.text, r.status_code)

