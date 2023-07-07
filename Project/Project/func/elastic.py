import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func.mecab import TextPreprocessing
from elasticsearch import Elasticsearch 


class ElasticSearchIndex:
    def __init__(self, elastic_url):
        self.es = Elasticsearch([elastic_url])

    # 인덱스 생성시 필요한 정보
    def index_poem(self, index_name, doc_id, poem, preprocessor):
                
        # 품사 태깅후 필요한 품사들만 추출
        VA_words = preprocessor.process_adjectives()
        VV_words = preprocessor.process_verbs()
        NNG_words = preprocessor.process_common_nouns()
        NNP_words = preprocessor.process_proper_nouns()
        MAG_words = preprocessor.process_common_adverbs()


        poem = {
            "VA": VA_words,
            "VV": VV_words,
            "NNG": NNG_words,
            "NNP": NNP_words,
            "MAG": MAG_words,
        }
        data = self.es.index(index=index_name, id=doc_id, body=poem)
        return data


