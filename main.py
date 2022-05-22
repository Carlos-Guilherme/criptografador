from asyncore import write
import os
import cryptocode
from PySimpleGUI import PySimpleGUI as sg
from pygame import WINDOWCLOSE

msg_cripto_text = open('msg_cripto_text.txt', 'a')
msg_decripto_text = open('msg_decripto_text.text', 'a')

def escolha():
    sg.theme('Black')
    linha = [
    [sg.Button('Criptografador', size = (200))],
    [sg.Button('Descriptografador', size = (200))]

    ]
    layout_escolha = [
        [sg.Frame('', layout = linha, key = 'container', size = (200, 70))]
    ]
    return sg.Window('Criptografador', layout = layout_escolha, finalize = True)

def criptografar():
    sg.theme('Black')
    linha = [
    [sg.Text('Insira o Texto a ser CRIPTOGRAFADO:')],
    [sg.Input(key = 'texto_a_ser_criptografado', size = (200, 200))],
    [sg.Text('Insira a Senha:')],
    [sg.Input(key = 'senha_da_mensagem', size = (200, 200))],
    [sg.Button('Criptografar Mensagem', size = (200))],

    ]
    layout_cripto = [
        [sg.Frame('', layout = linha, key = 'container', size = (300, 150))]
    ]
    return sg.Window('Criptografador', layout = layout_cripto, finalize = True)

def descriptografar():
    sg.theme('Black')
    linha = [
    [sg.Text('Insira o Texto a ser DESCRIPTOGRAFADO:')],
    [sg.Input(key = 'texto_a_ser_descriptografado', size = (200, 200))],
    [sg.Text('Insira a Senha:')],
    [sg.Input(key = 'senha_a_ser_chaveada', size = (200, 200))],
    [sg.Button('Descriptografar Mensagem', size = (200))],
    ]
    layout_decripto = [
        [sg.Frame('', layout = linha, key = 'container', size = (300, 150))]
    ]
    return sg.Window('Criptografador', layout = layout_decripto, finalize = True)

def mostrar_msg_cripto(a):
    sg.theme('Black')
    linha = [
    [sg.Text(a)],
    [sg.Button('Salvar Texto Criptografado', size = (500, 50))]

    ]
    layout_escolha = [
        [sg.Frame('', layout = linha, size = (350, 75))]
    ]
    return sg.Window('Mensagem Criptografada', layout = layout_escolha, finalize = True)

def mostrar_msg_descripto(a):
    sg.theme('Black')
    linha = [
    [sg.Text(a)],
    [sg.Button('Salvar Texto Descriptografado', size = (350, 50))]

    ]
    layout_escolha = [
        [sg.Frame('', layout = linha, size = (500, 75))]
    ]
    return sg.Window('Mensagem Descriptografada', layout = layout_escolha, finalize = True)

janela = escolha()


while True:
    eventos_ecolha1, valores_ecolha1 = janela.read()
    if eventos_ecolha1 == sg.WINDOW_CLOSED:
        break
    elif eventos_ecolha1 == 'Criptografador':
        janela.close()
        janela = criptografar()
        while True: 
            eventos_ecolha2, valores_ecolha2 = janela.read()
            if eventos_ecolha2 == sg.WINDOW_CLOSED:
                break
            elif eventos_ecolha2 == 'Criptografar Mensagem':
                texto_a_ser_criptografado = valores_ecolha2['texto_a_ser_criptografado']
                senha_da_mensagem = valores_ecolha2['senha_da_mensagem']
                msg_criptografada = cryptocode.encrypt(texto_a_ser_criptografado, senha_da_mensagem)
                janela.close() # criar uma janela que mostre o texto criptografado e mostre um botão que ao clicar salve em um bloco de texto
                janela = mostrar_msg_cripto(msg_criptografada)
                while True:
                    eventos_ecolha3, valores_ecolha3 = janela.read()
                    if eventos_ecolha3 == sg.WINDOW_CLOSED:
                        break
                    elif eventos_ecolha3 == 'Salvar Texto Criptografado':
                        msg_cripto_text.write(msg_criptografada)
    elif eventos_ecolha1 == 'Descriptografador':
        janela.close()
        janela = descriptografar()
        while True: 
            eventos_ecolha2, valores_ecolha2 = janela.read()
            if eventos_ecolha2 == sg.WINDOW_CLOSED:
                break
            elif eventos_ecolha2 == 'Descriptografar Mensagem':
                texto_a_ser_descriptografado = valores_ecolha2['texto_a_ser_descriptografado']
                senha_para_descriptografar = valores_ecolha2['senha_a_ser_chaveada']
                msg_descriptografada = cryptocode.decrypt(texto_a_ser_descriptografado, senha_para_descriptografar)
                janela.close() # criar uma janela que mostre o texto descriptografado e mostre um botão que ao clicar salve em um bloco de texto
                janela = mostrar_msg_descripto(msg_descriptografada)
                while True:
                    eventos_ecolha3, valores_ecolha3 = janela.read()
                    if eventos_ecolha3 == sg.WINDOW_CLOSED:
                        break
                    elif eventos_ecolha3 == 'Salvar Texto Descriptografado':
                        msg_decripto_text.write(msg_descriptografada)
            
