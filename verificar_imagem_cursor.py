import datetime
import time
import PIL.ImageShow
import pyautogui
import pyautogui as pa
import pytesseract.pytesseract
from PIL import ImageGrab, ImageEnhance, ImageOps
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'



cor_branca = False

while cor_branca == False:
    x, y = pyautogui.position()
    print(x, y)
    cor = pyautogui.pixel(x, y)
    print(cor)
    time.sleep(2)
    if pa.pixelMatchesColor(x, y, (231,243,255)):
        cor_branca = True

