from tika import parser
import easyocr
import cv2
import numpy as np
import magic
from pdf2image import convert_from_path
import mimetypes


class TextExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tk_contents = None

    def process_file(self):
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(self.file_path)

        if file_type == "application/pdf" or mimetypes.guess_type(self.file_path)[0] == "application/pdf":
            self.extract_text_from_pdf(file_path)
        elif file_type == "image/jpeg" or file_type == "image/png" :
            self.extract_text_from_image(file_path)
        else:
            print("옳바른 파일형식이 아닙니다..")
        return self.tk_contents

    def extract_text_from_pdf(self):
        # PDF 파일 TEXT 추출
        raw_pdf = parser.from_file(self.file_path)
        tk_contents = raw_pdf['content']
        self.tk_contents = tk_contents.strip()
        return self.tk_contents
       

        if self.tk_contents is None:
            print("이미지 PDF파일입니다.")
            
            reader = easyocr.Reader(['ko'])

            # Change PDF file to images
            images = convert_from_path(self.file_path)

            self.tk_contents = []  # Use multiple pages

            for page_num, img in enumerate(images):
                # OpenCV 형태로 변환
                img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
                # gray가 평균적으로 더 잘 추출함
                img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
                # EasyOcr 사용
                ocr_contents = reader.readtext(img_gray)
                # EasyOcr 여러 결과값 중 텍스트만 저장
                page_text = [result[1] for result in ocr_contents]
                self.tk_contents.extend(page_text)
            # tk_contents 문자형으로 변경
            self.tk_contents = '\n'.join(self.tk_contents)
            self.tk_contents = self.tk_contents.replace("\\", "").replace("\'", "")
            return self.tk_contents

    def extract_text_from_image(self):
        # EasyOCR Reader
        reader = easyocr.Reader(['ko'])

        img = cv2.imread(self.file_path)
        # gray가 평균적으로 더 잘 추출함
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # EasyOCR 사용
        ocr_contents = reader.readtext(img_gray)
        # EasyOcr 여러 결과값 중 텍스트만 저장
        self.tk_contents = [result[1] for result in ocr_contents]
        self.tk_contents = '\n'.join(self.tk_contents)
        return self.tk_contents





