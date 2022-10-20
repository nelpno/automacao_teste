import time
import PIL.ImageShow
import pyautogui as pa
import pytesseract.pytesseract
from PIL import ImageGrab, ImageEnhance, ImageOps
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

cor_branca = False

while cor_branca == False:
    x, y = pa.position()
    print(x, y)
    time.sleep(1)
    if pa.pixelMatchesColor(x, y, (255, 255, 255)):
        cor_branca = True

