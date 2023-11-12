import requests

base_url = "http://127.0.0.1:5000"

url = f"{base_url}/api/v1/documents/"
response = requests.post(url, json={"source": "aarni", "texts": ["I like cooking.", "I like steel manufacturing", "Steel manufacturing rocks!"]})
# print(response.text)
# print(response.json())

url = f"{base_url}/api/v1/documents/search/"
response = requests.post(url, json={"conversation_id": 1, "query": "How much does steel manufacturing rock?"})
print(response.text)
result = response.json()
print(result)

document = result["documents"][0]
document_id = document["id"]
query_id = result["query"]["id"]
document["reliability"] = 0.7
document["impact"] = -0.5
url = f"{base_url}/api/v1/queries/{query_id}/documents/{document_id}/"
response = requests.put(url, json=document)
print(response.json())

url = f"{base_url}/api/v1/queries/"
response = requests.get(url)
result = response.json()
print(result)

query_id = result[0]["id"]
url = f"{base_url}/api/v1/queries/{query_id}/"
response = requests.get(url)
result = response.json()
print(result)

# url = f"{base_url}/api/v1/trends/"
# response = requests.post(
#     url,
#     json={
#         "title": "My Trend",
#         "description": "My description",
#         "keywords": ["kw"],
#         "urls": None,
#         "scrape_interval": "daily",
#     },
# )
# trend = response.json()
# print(trend)

# url = f"{base_url}/api/v1/trends/"
# response = requests.get(url)
# print(response.json())

# trend_id = trend["id"]

# trend_id = 1
# url = f"{base_url}/api/v1/trends/{trend_id}"
# response = requests.put(
#     url,
#     json={
#         "id": trend_id,
#         "title": "My Trend Updated",
#         "description": "My description",
#         "keywords": ["kw2"],
#         "urls": None,
#         "scrape_interval": "daily",
#     },
# )
# print(response.json())

# url = f"{base_url}/api/v1/trends/{trend_id}/"
# response = requests.delete(url)
# print(response.status_code)

# url = f"{base_url}/api/v1/trends/"
# response = requests.get(url)
# print(response.json())

# Faiss({
#     "content": p
# })

# with open("/Users/aarni/projects/datascience/output.txt") as f:
#     p = f.read().splitlines()

# print(p)


# def t(a):
#     b = time.time()
#     print(b - a)
#     return b


# from txtai.embeddings import Embeddings
# import time

# a = t(time.time())
# embeddings = Embeddings()
# a = t(a)
# embeddings.index(p)
# a = t(a)
# output = embeddings.search("How much does steel manufacturing rock?")
# a = t(a)

# print(output)
