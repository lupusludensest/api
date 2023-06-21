import requests

# r = requests.get('https://httpbin.org/delay/1', timeout=3) # respond 200 OK after 1 second
# r = requests.get('https://httpbin.org/delay/2', timeout=3) # respond 200 OK after 2 second
r = requests.get('https://portal.18wheelerschool.com/login', timeout=3) # requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=3)

print(r.status_code)