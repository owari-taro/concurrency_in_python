
import requests

url = 'http://www.google.com'

res = requests.get(url)
print("status_code\n")
print(res.status_code)
print("headers\n")
print(res.headers)

with open('google.html', 'w') as f:
    f.write(res.text)

print('Done.')