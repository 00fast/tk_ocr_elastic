from func.seach import Elasticsearch_Indexsearch
from gensim.models import Word2Vec

if __name__ == "__main__":
    # 엘라스틱서치, word2vec 모델
    search = Elasticsearch_Indexsearch("http://34.64.154.112:9200", "word2vec.model")

    # 검색조건
    index_name = "words"
    Key = "words"
    Value = "사랑"
    
    
    # 검색 결과 및 json 저장에 필요
    hits = search.es_search(index_name, Key, Value)

    # 검색한 Value와 연관성 있는 단어 추천
    search.find_similar(Value)

    

