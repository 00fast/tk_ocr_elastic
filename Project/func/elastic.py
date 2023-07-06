import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func.mecab import TextPreprocessing
from elasticsearch import Elasticsearch 


class ElasticSearchIndex:
    def __init__(self, elastic_url):
        self.es = Elasticsearch([elastic_url])

    def index_poem(self, index_name, doc_id, poem):
        data = self.es.index(index=index_name, id=doc_id, body=poem)
        return data




# idex 확인하는 출력문 

# index_name = "index_name"

# # 사이즈 만큼 데이터 출력 (데이터 입력되었는지 확인)
# query = {
#     "query": {
#         "match_all": {}
#     },
# 	"size": 1000 
# }


# results = es.search(index=index_name, body=query)


# hits = results["hits"]["hits"]


# for hit in hits:
#     print("Document ID:", hit["_id"])
#     print("Data:", hit["_source"])
#     print()