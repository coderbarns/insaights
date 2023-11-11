import requests

base_url = "http://127.0.0.1:5000"

url = f"{base_url}/api/v1/embeddings/index/"

response = requests.post(url, json={"text": "Hello, world!"})
print(response)
# print(response.json())
