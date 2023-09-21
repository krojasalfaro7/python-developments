import pdf2image
import pytesseract
from pytesseract import Output, TesseractError

pdf_path = "/home/kevin/Repository/python-developments/PDF/document.pdf"

images = pdf2image.convert_from_path(pdf_path)

pil_im = images[0] # assuming that we're interested in the first page only

ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
# ocr_dict now holds all the OCR info including text and location on the image

text = " ".join(ocr_dict['text'])
