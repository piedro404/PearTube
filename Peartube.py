from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolButton, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QLine, QUrl, QSize, qInf
from PyQt5.QtGui import QIcon, QPixmap, qPixelFormatAlpha
import youtube_dl
import os
from youtube_dl.utils import DownloadError 
import threading

application = QApplication([])

#Redimencionando a Janela Princial
mainWindow = QMainWindow()
mainWindow.setGeometry(0, 0, 850, 650)
mainWindow.setMinimumHeight(650)
mainWindow.setMaximumHeight(650)
mainWindow.setMinimumWidth(850)
mainWindow.setMaximumWidth(850)

#Custimização da Janela
mainWindow.setWindowTitle("Peartube Download")
mainWindow.setStyleSheet("background-color: rgb(200,40,35);")
mainWindow_icon = QIcon()
mainWindow_icon.addPixmap(QPixmap("./src/icones/pear.png"))
mainWindow.setWindowIcon(mainWindow_icon)

background = QLabel(mainWindow)
background.setStyleSheet("background-color: rgb(255,255,255);")
background.resize(850, 650)
background.move(0,0)
background.setPixmap(QPixmap('./src/icones/background.png'))

#URL
web = QWebEngineView(mainWindow)
web.setStyleSheet("background-color: rgb(255, 255, 255);")
web.setGeometry(105, 80, 630, 270)
web.load(QUrl("https://www.youtube.com"))


#Error
error = QLabel(mainWindow)
error.setStyleSheet("QLabel { background-color : transparent; color : black; font-size : 25px;}")
error.resize(500,50)

#Msg
msg = QLabel(mainWindow)
msg.setStyleSheet("QLabel { background-color : transparent; color : black; font-size : 25px;}")
msg.resize(500,50)

#Botão de Barra de Pesquisa
go_line = QLineEdit(mainWindow)
go_line.setGeometry(115, 30, 610, 45)
go_line.setStyleSheet("background-color: rgb(255,255,255); font-size: 20px;")


#Botão de Pesquisa
go_button = QToolButton(mainWindow)
go_button.setGeometry(725, 27, 50, 50)
go_button_icon = QIcon()
go_button_icon.addPixmap(QPixmap("./src/icones/go.png"))
go_button.setIcon(go_button_icon)
go_button.setStyleSheet("background-color: transparent;")
go_button.setIconSize(QSize(40, 40))

#Botão Icon do MP3
mp3_button = QToolButton(mainWindow)
mp3_button.setGeometry(225, 350, 110, 130)
mp3_button_icon = QIcon()
mp3_button_icon.addPixmap(QPixmap("./src/icones/mp3.png"))
mp3_button.setIcon(mp3_button_icon)
mp3_button.setStyleSheet("background-color: transparent;")
mp3_button.setIconSize(QSize(125, 125))

#Botão Icon do MP4
mp4_button = QToolButton(mainWindow)
mp4_button.setGeometry(525, 350, 110, 130)
mp4_button_icon = QIcon()
mp4_button_icon.addPixmap(QPixmap("./src/icones/mp4.png"))
mp4_button.setIcon(mp4_button_icon)
mp4_button.setStyleSheet("background-color: transparent;")
mp4_button.setIconSize(QSize(125, 125))

#Botão Icon do Download
dl_button = QToolButton(mainWindow)
dl_button.setGeometry(362.5, 500, 110, 130)
dl_button_icon = QIcon()
dl_button_icon.addPixmap(QPixmap("./src/icones/download.png"))
dl_button.setIcon(dl_button_icon)
dl_button.setStyleSheet("background-color: transparent;")
dl_button.setIconSize(QSize(125, 125))

#Botão Icon do Path
path_button = QToolButton(mainWindow)
path_button.setGeometry(745, 540, 100, 100)
path_button_icon = QIcon()
path_button_icon.addPixmap(QPixmap("./src/icones/pasta.png"))
path_button.setIcon(path_button_icon)
path_button.setStyleSheet("background-color: transparent;")
path_button.setIconSize(QSize(100, 100))

#Funções
global typey
typey = None

def go(mainWindow):
    web.load(QUrl())
    error.setText("")
    error.move(-100,-100)
    msg.setText("")
    msg.move(-100,-100)
    #https://www.youtube.com/watch?v=ucsadKDNTQA
    go_url = go_line.text()
    request1 = "https://www.youtube.com/watch?"
    request2 = "https://youtu.be/"
    go_len = len(go_url)
    if((request1 in go_url and go_url[0:30] == request1 and go_len > 30) or (request2 in go_url and go_url[0:17] == request2 and go_len > 17)):
        web.load(QUrl(go_url))
    else:
        error.setText("A URL do Youtube é Invalida!")
        error.move(270,-10)

def path(mainWindow):
    error.setText("")
    error.move(-100,-100)
    msg.setText("")
    msg.move(-100,-100)
    os.startfile("")


def mp3(mainWindow):
    global typey
    error.setText("")
    error.move(-100,-100)
    msg.setText("")
    msg.move(-100,-100)
    typey = "MP3"
    #print(type)

def mp4(mainWindow):
    global typey
    error.setText("")
    error.move(-100,-100)
    msg.setText("")
    msg.move(-100,-100)
    typey = "MP4"
    #print(type)
    
def download():
    global typey
    #https://www.youtube.com/watch?v=wdJvZnHdsvM
    error.setText("")
    error.move(-100,-100)
    msg.setText("")
    msg.move(-100,-100)
    url = go_line.text()
    request1 = "https://www.youtube.com/watch?"
    request2 = "https://youtu.be/"
    lenurl = len(url)

    #print(request in url and url[0:30] == request and lenurl > 29)
    if((request1 in url and url[0:30] == request1 and lenurl > 30) or (request2 in url and url[0:17] == request2 and lenurl > 17)):
        type=typey
        if type == "MP3":
            msg.move(230,610)
            msg.setText(f"Download da Vídeo foi Iniciado!")
            try:
                #os.chdir("C:\Users\Mpedr\Documents\Projetos Programação\Testes\Youtube Player Download")
                info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
                filename = f"{info['title']}.mp3"
                path = (QFileDialog.getSaveFileName(None, "Salvar Aonde?", filename))

                options = {
                    'format' : 'bestaudio/best',
                    'keepvideo': False,
                    'outtmpl': path[0],
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192'
                    }]
                }
                
                with youtube_dl.YoutubeDL(options) as ydl:
                    ydl.download([info['webpage_url']])
                msg.setText(f"Download da Música foi Concluido!")
                #print(f"\n\nDownload da Música ({info['title']}) foi Concluido!\n")

            except DownloadError:
                error.setText(f"Houve Algum Erro, Verifique sua URL ou sua Conexão a Internet e Tente Novamente!")
                error.move(270,-10)
                #print(f"\n\n    OPSS.... \n Houve Algum erro, Verifique sua URL ou sua Conexão a Internet e Tente Novamente!\n")

        elif type == "MP4":
            msg.move(230,610)
            msg.setText(f"Download da Vídeo foi Iniciado!")
            try:
                info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
                filename = f"{info['title']}.mp4"
                path = (QFileDialog.getSaveFileName(None, "Salvar Aonde?", filename))

                options = {
                    'format' : '136+bestaudio[ext=m4a]/mp4',
                    'outtmpl': path[0],
                }
                
                with youtube_dl.YoutubeDL(options) as ydl:
                    ydl.download([info['webpage_url']])
                msg.setText(f"Download do Vídeo foi Concluido!")
                #print(f"\n\nDownload do Vídeo ({result['Título']}) foi Concluido!\n")
            except:
                error.setText(f"Houve Algum Erro!")
                error.move(280,-10)
                #print(f"\n\n    OPSS.... \n Houve Algum erro, Verifique sua URL ou sua Conexão a Internet e Tente Novamente!\n")
        else:
            error.setText("Você tem que Escolher um Tipo de Arquivo!")
            error.move(180,-10)
            #print("\n\nVocê tem que Escolher um Tipo de Arquivo!\n")
    else:
        error.setText("A URL do Youtube é Invalida!")
        error.move(270,-10)

def download_e(mainWindow):
    threading.Thread(target=download).start()

#Conectado as Funções aos Botãos  
go_button.clicked.connect(go)
path_button.clicked.connect(path)
mp3_button.clicked.connect(mp3)
mp4_button.clicked.connect(mp4)
dl_button.clicked.connect(download_e)


#Exibir
mainWindow.show()
application.exec_()

