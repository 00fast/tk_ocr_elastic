from func.mecab import TextPreprocessing
from func.tk_ocr import TextExtractor
from func.elastic import ElasticSearchIndex

# main 예시
if __name__ == "__main__":
    # 사용할 File_path와 elastic url
    file_path = "D:/work/nlp/Text Mining/text_preprocessing/Project/poem.pdf"
    elastic_url = "http://34.64.154.112:9200"

    
    indexer = ElasticSearchIndex(elastic_url)

    
    # file_path의 파일 형식에 따른 tika text 추출
    extractor = TextExtractor(file_path)
    tk_contents = extractor.process_file(file_path)

    # tk_contents를 토크나이저 및 불용어 제거
    preprocessor = TextPreprocessing(tk_contents)

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

    # 원하는 인덱스 정보들
    index_name = "test_Pome"
    doc_id = "유명_시"
    data = indexer.index_poem(index_name, doc_id, poem)