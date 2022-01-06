import requests

url = 'http://google.com'
response = request.get(url)
print(f'Response return: {response.status_code}, {response.reason}')
print (response.text)