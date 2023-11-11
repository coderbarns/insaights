import requests
from txtai.ann import Faiss

base_url = "http://127.0.0.1:5000"

url = f"{base_url}/api/v1/documents/"
response = requests.post(url, json={"source": "aarni", "texts": ["I like cooking.", "I like steel manufacturing", "Steel manufacturing rocks!"]})
print(response.json())

url = f"{base_url}/api/v1/documents/search/"
response = requests.post(url, json={"query": "How much does steel manufacturing rock?"})
print(response.json())


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
