from func.mecab import TextPreprocessing
from func.tk_ocr import TextExtractor
from func.elastic import ElasticSearchIndex

# main 예시
if __name__ == "__main__":
    # 사용할 File_path와 elastic url
    file_path = "D:/work/nlp/Text Mining/text_preprocessing/Project/jpgpoem.jpg"
    elastic_url = "http://34.64.154.112:9200"

        
    indexer = ElasticSearchIndex(elastic_url)

        
    # file_path의 파일 형식에 따른 tika text 추출
    extractor = TextExtractor(file_path)
    tk_contents = extractor.process_file()

    # tk_contents를 토크나이저 및 불용어 제거
    preprocessor = TextPreprocessing(tk_contents)

    
    # 원하는 인덱스 정보들
    index_name = "text_test"
    doc_id = "이미지시"
    data = indexer.index_poem(index_name, doc_id, preprocessor, preprocessor)

