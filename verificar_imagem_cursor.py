from datetime import datetime
import time
import PIL.ImageShow
import pyautogui
import pyautogui as pa
import pytesseract.pytesseract
from PIL import ImageGrab, ImageEnhance, ImageOps
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def verificar_cor_eixo(r, g, b):
    achou_cor = False

    while not achou_cor:
        x, y = pyautogui.position()
        print(x, y)
        cor = pyautogui.pixel(x, y)
        print(cor)
        time.sleep(2)
        if pa.pixelMatchesColor(x, y, (r, g, b)):
            achou_cor = True

def verificar_cor_pixel(x, y, r, g, b):
    achou_cor = False

    while not achou_cor:
        if pa.pixelMatchesColor(x, y, (r, g, b)):
            achou_cor = True

    return True

# while not verificar_cor_eixo(255, 255, 255):
verificar_cor_eixo(255, 255, 255)


def tempo(segundos):
    pyautogui.countdown(segundos)


def press_junto(letras):
    pyautogui.hotkey(letras)


def apertar(letra):
    pyautogui.press(letra)


def escreve(texto):
    pyautogui.write(texto)


def imagem_clicar(arquivo):
    achar_arquivo = pyautogui.locateOnScreen(arquivo)
    pyautogui.click(achar_arquivo)


def data_hoje():
    data_atual = datetime.today()
    data_em_texto = data_atual.strftime('%d-%m-%Y')
    return data_em_texto
