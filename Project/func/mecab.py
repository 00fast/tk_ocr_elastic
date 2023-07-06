from konlpy.tag import Mecab
from func.tk_ocr import TextExtractor
import re

class TextPreprocessing:
    def __init__(self, tk_contents):
        self.mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
        self.tk_contents = tk_contents
        self.processed_stop_words = self.preprocess_stop_words()
        # 토크나이저 및 불용어 제거

    def preprocess_stop_words(self):  
        text = self.tk_contents.strip()  
        stopword_dic = ['to', 'to', 'this', 'to', 'to', 'to', 'null', '/', '-', '&', '�' '(', ')', '.', ',']
        text = re.sub('[^가-힣]', ' ', text)  # Remove all other characters except for Korean characters
        tokens = self.mecab.morphs(text)
        result = [word for word in tokens if word not in stopword_dic]
        processed_stop_words = ' '.join(result)
        return processed_stop_words

        # 품사태깅
        # mecab_pos = self.mecab.pos(self.processed_stop_words)

    # 일반명사
    def process_common_nouns(self):
        NNG_tag = ['NNG']
        NNG_words = tuple(word for word, tag in self.mecab.pos(self.processed_stop_words) if tag in NNG_tag)
        
        return NNG_words

    # 고유명사
    def process_proper_nouns(self):
        
        NNP_tag = ['NNP']
        NNP_words = tuple(word for word, tag in self.mecab.pos(self.processed_stop_words) if tag in NNP_tag)
        
        return NNP_words

    # 동사
    def process_verbs(self):
        
        VV_tag = ['VV']
        VV_words = tuple(word for word, tag in self.mecab.pos(self.processed_stop_words) if tag in VV_tag)
        
        return VV_words

    # 형용사
    def process_adjectives(self):
        
        VA_tag = ['VA']
        VA_words = tuple(word for word, tag in self.mecab.pos(self.processed_stop_words) if tag in VA_tag)
        
        return VA_words

    # 일반부사
    def process_common_adverbs(self):
        
        MAG_tag = ['MAG']
        MAG_words = tuple(word for word, tag in self.mecab.pos(self.processed_stop_words) if tag in MAG_tag)
        
        return MAG_words


