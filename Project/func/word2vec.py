from elasticsearch import Elasticsearch, helpers
from gensim.models import Word2Vec

import numpy as np

# Connect to Elasticsearch
es = Elasticsearch(["http://34.64.154.112:9200"])

# Define the index to scan
index_name = "words"

# Use scan method to get all documents
actions = helpers.scan(es,
    index=index_name,
    query={"query": {"match_all": {}}},
)

# Get documents words
docs = [action['_source']['words'] for action in actions]

# Already preprocessed words
sentences = docs

# Train Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=5, workers=4 , epochs=30)

# Save the model
model.save("word2vec.model")
