import requests

# payload = {'page': 2, 'count': 25}
payload = {'user_name': 'corey', 'password': '_testing'} # https://httpbin.org/basic-auth/corey/_testing

# r = requests.get('https://xkcd.com/353/')
# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# r = requests.get('https://httpbin.org/get/get?page=2&count=25')
# r = requests.get('https://httpbin.org/get', params=payload)
r = requests.post('https://httpbin.org/post', data=payload)

# print(dir(r))
# print(help(r))
# print(r.text)
# print(r.content)
# with open('comic.png', 'wb') as f:
#     f.write(r.content)
# print(r.status_code)
# print(r.ok)
# print(r.headers)
# print(r.text)
# print(r.url)
# print(r.text)
# print(r.json())
r_dict = r.json()
print(r_dict['form'])
