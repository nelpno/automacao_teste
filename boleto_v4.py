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
    escreve("https://business.facebook.com/ads/manager/billing_history/summary/?act={:.0f} ".format(id_lista[i]))
    time.sleep(.25)
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
    tempo(11)

    if verificar_imagem('gerar_boleto_caminho_2.png') is not None:
        imagem_clicar('gerar_boleto_caminho_2.png')
        pyautogui.scroll(-250)
        while verificar_imagem('ver_meu_boleto_2.png') is None:
            print('Não achei. 70')
            time.sleep(0.2)
        imagem_clicar('ver_meu_boleto_2.png')
        while verificar_imagem('salvar_boleto_em_pdf.png') is None:
            print('Não achei. 4')
            time.sleep(0.2)
            imagem_clicar('salvar_boleto_em_pdf.png')
        while verificar_imagem('abriu_boleto_2.png') is None:
            print('Não achei. 5')
            time.sleep(0.2)

        apertar('backspace')
        escreve("{} facebook".format("{}_{}-{}".format(valor_lista[i], cliente_lista[i], data_hoje())))
        time.sleep(.25)
        imagem_clicar('downloads.png')
        time.sleep(.25)
        imagem_clicar('salvar.png')
        time.sleep(.25)
        pyautogui.click(3417, 1369)
        press_2_teclas('ctrl', 'f4')
        time.sleep(.25)
        imagem_clicar('navegador.png')

    else:
        while verificar_imagem('baixar.png') is None:
            print('Não achei. 4')
            time.sleep(0.2)
        imagem_clicar('baixar.png')
        while verificar_imagem('abriu_boleto.png') is None:
            print('Não achei. 5')
            time.sleep(0.2)
        escreve("{} facebook".format("{}_{}-{}".format(valor_lista[i], cliente_lista[i], data_hoje())))
        imagem_clicar('downloads.png')
        time.sleep(.25)
        press_2_teclas('alt', 'l')
        time.sleep(.25)
        imagem_clicar('x_boleto_feito.png')
        pyautogui.click(3417, 1369)
        imagem_clicar('navegador.png')


# lista de clientes puxada pelo Excel
i = 0
df = pd.read_excel('teste.xlsx')
cliente_lista = df['Cliente'].tolist()
id_lista = df['ID'].tolist()
valor_lista = df['Valor'].tolist()


print(id_lista[0])
# inicio abrindo navegador
imagem_clicar('chrome_nelson.png')

while verificar_imagem('chrome_abriu.png') is None:
    time.sleep(0.2)

press_2_teclas('ctrl', 'f4')
time.sleep(0.25)

while verificar_imagem("clicar_navegador.png") is None:
    time.sleep(0.25)

imagem_clicar('clicar_navegador.png')

while i < len(cliente_lista):
    criar_boletos(i)
    i += 1

imagem_clicar("documentos.png")
while verificar_imagem("downloads.png") is None:
    time.sleep(0.25)
imagem_clicar("downloads.png")
