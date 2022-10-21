import time
import PIL.ImageShow
import pyautogui as pa
import pytesseract.pytesseract
from PIL import ImageGrab, ImageEnhance, ImageOps
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#Pegar screenshot completo
img = ImageGrab.grab()

#Recortar o screenshoot nas coordenadas
img = img.crop((1803, 906, 2420, 1024))
PIL.ImageShow.show(img)

width, height = img.size
print(width, height)
imgdata = pytesseract.image_to_data(img, lang="pt-br")