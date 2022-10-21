import time
from datetime import datetime

import pyautogui
import pyautogui as pa


def tempo(segundos):
    pyautogui.countdown(segundos)


def press_2_teclas(letra1, letra2):
    pyautogui.hotkey(letra1, letra2)


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


def verificar_cor_pixel(x, y, r, g, b):
    achou_cor = False

    while not achou_cor:
        if pa.pixelMatchesColor(x, y, (r, g, b)):
            achou_cor = True

    return True


cliente = "Maxi Massas"
valor_investido = "400,00"

escrita_boleto = ("{}-{}".format(cliente, data_hoje()))

imagem_clicar('chrome_nelson.png')
tempo(2)
press_2_teclas('ctrl', 'f4')
tempo(1)
escreve("https://business.facebook.com/ads/manager/billing_history/summary/?act=704083103754311")
apertar("enter")
tempo(5)
imagem_clicar('adicionar_fundos.png')
tempo(5)
apertar('tab')
press_2_teclas('ctrl', 'a')
apertar('backspace')
escreve(valor_investido)
imagem_clicar('boleto_bancario.png')
imagem_clicar('adicionar_fundos_2.png')

while not verificar_cor_pixel(2515, 771, 231, 243, 255):
    verificar_cor_pixel(2515, 771, 231, 243, 255)

imagem_clicar('baixar.png')
tempo(2)
escreve(escrita_boleto)
imagem_clicar('downloads.png')
tempo(2)
press_2_teclas('alt', 'l')
tempo(1)
imagem_clicar('x_boleto_feito.png')

# https://business.facebook.com/ads/manager/billing_history/summary/?act=704083103754311 LINK RESUMIDO ID DO CLIENTE
