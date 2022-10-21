import time
from datetime import datetime

import pyautogui
import pyautogui as pa
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

data_atual = datetime.today()
data_em_texto = data_atual.strftime('%d-%m-%Y')

cliente = "Maxi Massas"
valor_investido = "400,00"

escrita_boleto = ("{}-{}".format(cliente, data_em_texto))

abrir_chrome = pyautogui.locateOnScreen('chrome_nelson.png')
pyautogui.click(abrir_chrome)
time.sleep(2)
pyautogui.hotkey('ctrl', 'f4')
pyautogui.countdown(1)
pyautogui.write("https://business.facebook.com/ads/manager/billing_history/summary/?act=704083103754311")
pyautogui.press("enter")
pyautogui.countdown(5)
adicionar_fundos = pyautogui.locateOnScreen('adicionar_fundos.png')
pyautogui.click(adicionar_fundos)
pyautogui.countdown(5)
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')
pyautogui.write(valor_investido)
clicar_boleto = pyautogui.locateOnScreen('boleto_bancario.png')
pyautogui.click(clicar_boleto)
adicionar_fundos_2 = pyautogui.locateOnScreen('adicionar_fundos_2.png')
pyautogui.click(adicionar_fundos_2)

cor_azul = False

while not cor_azul:
    x, y = (2506, 771)
    print(x, y)
    time.sleep(2)
    if pa.pixelMatchesColor(x, y, (231, 243, 255)):
        cor_azul = True

baixar_boleto = pyautogui.locateOnScreen('baixar.png')
pyautogui.click(baixar_boleto)

pyautogui.countdown(2)
pyautogui.write(escrita_boleto)

pasta_salvamento = pyautogui.locateOnScreen('downloads.png')
pyautogui.click(pasta_salvamento)
pyautogui.countdown(2)

pyautogui.hotkey('alt', 'l')
pyautogui.countdown(1)

fechar_boleto_feito = pyautogui.locateOnScreen('x_boleto_feito.png')
pyautogui.click(fechar_boleto_feito)

# Box(left=3351, top=3, width=40, height=34) Nova Guia Chrome

# pyautogui.moveTo(2009,50,2)

# https://business.facebook.com/ads/manager/billing_history/summary/?act=704083103754311&pid=p1&business_id=205744063478775&page=billing_history&tab=summary&date=1663898400_1666317600

# https://business.facebook.com/ads/manager/billing_history/summary/?act=704083103754311 LINK RESUMIDO
