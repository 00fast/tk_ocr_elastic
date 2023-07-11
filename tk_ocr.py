from tika import parser
import easyocr
import cv2
import numpy as np
import magic
from pdf2image import convert_from_path
import mimetypes
import time


class TextExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tk_contents = None
        self.reader = easyocr.Reader(['ko', 'en'])

    def process_file(self):
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(self.file_path)

        # 파일 type 별 text 추출 및 걸리는 시간 체크
        if file_type == "application/pdf" or mimetypes.guess_type(self.file_path)[0] == "application/pdf":
            start_time = time.time()
            self.extract_text_from_pdf(self.file_path)
            end_time = time.time() - start_time
        elif file_type == "image/jpeg" or file_type == "image/png" :
            start_time = time.time()
            self.extract_text_from_image(self.file_path)
            end_time = time.time() - start_time
        else:
            print("올바른 파일형식이 아닙니다..")

        num_pages = self.get_number_of_pages()

        print(f"PDF 페이지 수: {num_pages}")
        print(f"Text 추출 걸린 시간: {end_time} seconds")

        return self.tk_contents
        
    # PDF 파일 페이지 확인
    def get_number_of_pages(self):
        raw_pdf = parser.from_file(self.file_path, xmlContent=True)
        xml_content = raw_pdf['content']
        num_pages = xml_content.count('<div class="page">')

        return num_pages
    
    def extract_text_from_pdf(self, file_path):
        # PDF 파일 TEXT 추출
        raw_pdf = parser.from_file(self.file_path)
        tk_contents = raw_pdf['content']
        if tk_contents is not None:
            self.tk_contents = tk_contents.strip()
        else :     
       
            print("이미지 PDF파일입니다.")
            
            
            # PDF파일을 IMAGE로 변경
            images = convert_from_path(self.file_path)

            self.tk_contents = []  # 여러 페이지

            for page_num, img in enumerate(images):
                # OpenCV 형태로 변환
                img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
                # gray가 평균적으로 더 잘 추출함
                img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
                # EasyOcr 사용
                ocr_contents = self.reader.readtext(img_gray)
                # EasyOcr 여러 결과값 중 텍스트만 저장
                page_text = [result[1] for result in ocr_contents]
                self.tk_contents.extend(page_text)
            self.tk_contents = '\n'.join(self.tk_contents)
        
        return self.tk_contents

    def extract_text_from_image(self, file_path):
        # EasyOCR Reader
        
        img = cv2.imread(self.file_path)
        # gray가 평균적으로 더 잘 추출함
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # EasyOCR 사용
        ocr_contents = self.reader.readtext(img_gray)
        # EasyOcr 여러 결과값 중 텍스트만 저장
        self.tk_contents = [result[1] for result in ocr_contents]
        self.tk_contents = '\n'.join(self.tk_contents)
        return self.tk_contents



