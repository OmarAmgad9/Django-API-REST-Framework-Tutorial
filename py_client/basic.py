import requests


endpoint = "http://127.0.0.1:8000/api/"

re = requests.get(endpoint, params={'abc':123}, json={"query": "hello World"})

print(re.json()['message'])