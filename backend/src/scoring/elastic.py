from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from txtai.scoring import Scoring

class Elastic(Scoring):
  def __init__(self, config=None):
    # Scoring configuration
    self.config = config if config else {}

    # Server parameters
    self.url = self.config.get("url", "http://localhost:9200")
    self.indexname = self.config.get("indexname", "testindex")

    # Elasticsearch connection
    self.connection = Elasticsearch(self.url)

    self.terms = True
    self.normalize = self.config.get("normalize")

  def insert(self, documents, index=None):
    rows = []
    for uid, document, tags in documents:
        rows.append((index, document))

        # Increment index
        index = index + 1

    bulk(self.connection, ({"_index": self.indexname, "_id": uid, "text": text} for uid, text in rows))

  def index(self, documents=None):
    self.connection.indices.refresh(index=self.indexname)

  def search(self, query, limit=3):
    return self.batchsearch([query], limit)

  def batchsearch(self, queries, limit=3):
    # Generate bulk queries
    request = []
    for query in queries:
      req_head = {"index": self.indexname, "search_type": "dfs_query_then_fetch"}
      req_body = {
        "_source": False,
        "query": {"multi_match": {"query": query, "type": "best_fields", "fields": ["text"], "tie_breaker": 0.5}},
        "size": limit,
      }
      request.extend([req_head, req_body])

      # Run ES query
      response = self.connection.msearch(body=request, request_timeout=600)

      # Read responses
      results = []
      for resp in response["responses"]:
        result = resp["hits"]["hits"]
        results.append([(r["_id"], r["_score"]) for r in result])

      return results

  def count(self):
    response = self.connection.cat.count(self.indexname, params={"format": "json"})
    return int(response[0]["count"])

  def load(self, path):
    # No local storage
    pass

  def save(self, path):
    # No local storage
    pass