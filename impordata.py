import urllib.request
import json
 
url = "https://quote-api.dicoding.dev/list"
response = urllib.request.urlopen(url)
result = response.read().decode()
print(result)