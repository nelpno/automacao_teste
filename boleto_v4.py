import time
from datetime import datetime

import pyautogui
import pyautogui as pa
import pandas as pd


def tempo(segundos):
    pyautogui.countdown(segundos)


def press_2_teclas(letra1, letra2):
    pyautogui.hotkey(letra1, letra2)


def apertar(letra):
    pyautogui.press(letra)


def escreve(texto):
    pyautogui.write(texto)


def imagem_clicar(arquivo):
    achar_arquivo = pyautogui.locateOnScreen(arquivo, confidence=.99, grayscale=True)
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


def verificar_imagem(arquivo):
    achei = pyautogui.locateOnScreen(arquivo, confidence=.99, grayscale=True)
    return achei


def criar_boletos(i):
    escreve("https://business.facebook.com/ads/manager/billing_history/summary/?act={}".format(id_lista[i]))
    apertar("enter")
    tempo(2)
    while verificar_imagem('adicionar_fundos.png') is None:
        print('Não achei. 1')
        time.sleep(0.1)
    imagem_clicar('adicionar_fundos.png')
    while verificar_imagem('espera_adicionar_fundos.png') is None:
        print('Não achei. 2')
        time.sleep(0.1)
    apertar('tab')
    press_2_teclas('ctrl', 'a')
    apertar('backspace')
    escreve("{}".format(valor_lista[i]))
    imagem_clicar('boleto_bancario.png')
    imagem_clicar('adicionar_fundos_2.png')

    while verificar_imagem('baixar.png') is None:
        print('Não achei. 4')
        time.sleep(0.2)

    imagem_clicar('baixar.png')

    while verificar_imagem('abriu_boleto.png') is None:
        print('Não achei. 5')
        time.sleep(0.2)

    escreve("{}".format("{}-{}".format(cliente_lista[i], data_hoje())))
    imagem_clicar('downloads.png')
    time.sleep(.25)
    press_2_teclas('alt', 'l')
    time.sleep(.25)
    imagem_clicar('x_boleto_feito.png')
    pyautogui.click(3417, 1369)
    imagem_clicar('navegador.png')


i = 0

# lista de clientes puxada pelo Excel
df = pd.read_excel('teste.xlsx')  # can also index sheet by name or fetch all sheets
cliente_lista = df['Cliente'].tolist()
id_lista = df['ID'].tolist()
valor_lista = df['Valor'].tolist()

# inicio abrindo navegador
imagem_clicar('chrome_nelson.png')

while verificar_imagem('chrome_abriu.png') is None:
    time.sleep(0.1)

press_2_teclas('ctrl', 'f4')
time.sleep(0.1)

while i < len(cliente_lista):
    criar_boletos(i)
    i += 1

imagem_clicar("documentos.png")
while verificar_imagem("downloads.png") is None:
    time.sleep(0.25)
imagem_clicar("downloads.png")
