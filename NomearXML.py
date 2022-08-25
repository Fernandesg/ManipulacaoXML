import os
from xml.dom import minidom
import PySimpleGUIQt as sg
import smtplib

credencialEmail = open('credencialEmail.txt', 'r')
loginEmail = []

for linhas in credencialEmail:
    linhas = linhas.strip()
    loginEmail.append(linhas)
usuario_email = loginEmail[0][17:-1]
senha_email = loginEmail[1][15:-1]
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
s.login(usuario_email, senha_email)

layout=[
    [sg.Text('Selecionar pasta com os arquivos:')],
    [sg.Input('',key='-CAMINHOPASTA-'),sg.FolderBrowse()],
    [sg.Stretch() ,sg.Text('Inserir número da ND:'), sg.Stretch()],
    [sg.Stretch() ,sg.Input(key='-NUMND-'), sg.Stretch()],
    [sg.Stretch(), sg.Button('RENOMEAR', key='-RENOMEAR-' ,size=(15,1)), sg.Stretch()],
    [sg.Stretch(), sg.Text('', key='-AVISO-'), sg.Stretch()],

]

window = sg.Window('Renomear arquivos', layout= layout, size=(300, 200))

def obter_arquivos_xml(diretorio):
    ret = []
    for arq in os.listdir( diretorio ):
        if arq.endswith(".xml"):
            ret.append( os.path.join( diretorio, arq ) )
    return ret
while True:
    event, values = window.read()
    diretorio = values['-CAMINHOPASTA-'] 
    if event == None:
        break
    if event == sg.WIN_CLOSED:
        break
    if event == '-RENOMEAR-':
        for arquivos in obter_arquivos_xml(diretorio):
                xml = minidom.parse(arquivos)
                fornecedor = xml.getElementsByTagName('xNome')[0].firstChild.data
                nNF = xml.getElementsByTagName('nNF')[0].firstChild.data
                chaveNF = xml.getElementsByTagName('chNFe')[0].firstChild.data
                nd = values['-NUMND-']
                nomeCompleto = 'NF ' + nNF + ' ' + fornecedor + ' (REPASSE ND ' + nd + ')'
                #renomear
                file_oldname = os.path.join(diretorio, chaveNF+".pdf")
                file_newname_newfile = os.path.join(diretorio, nomeCompleto+'.pdf')
                os.rename(file_oldname, file_newname_newfile)
        window['-AVISO-'].update('ARQUIVOS RENOMEADOS!')