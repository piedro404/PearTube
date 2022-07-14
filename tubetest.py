import youtube_dl
import os
from youtube_dl.utils import DownloadError 


#https://www.youtube.com/watch?v=wdJvZnHdsvM
url = input("URL do Youtube: ")
request = "https://www.youtube.com/watch?"
lenurl = len(url)

#print(request in url and url[0:30] == request and lenurl > 29)
if(request in url and url[0:30] == request and lenurl > 30):
    type=input("\nTipo do Arquivo\nMP3 or MP4: ").upper()
    
    if type == "MP3":
        try:
            info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
            if not os.path.exists("Downloads/mp3"):
                os.makedirs("Downloads/mp3")
            os.chdir("./")
            os.chdir("./Downloads/mp3")
            filename = f"{info['title']}.mp3"
            options = {
                'format' : 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': filename,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }]
            }
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([info['webpage_url']])
            print(f"\n\nDownload da Música ({info['title']}) foi Concluido!\n")

        except DownloadError:
            print(f"\n\n    OPSS.... \n Houve Algum erro, Verifique sua URL ou sua Conexão a Internet e Tente Novamente!\n")

    elif type == "MP4":
        try:
            info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
            if not os.path.exists("Downloads/mp4"):
                os.makedirs("Downloads/mp4")
            os.chdir("./")
            os.chdir("./Downloads/mp4")
            filename = f"{info['title']}.mp4"
            options = {
                'format' : '136+bestaudio[ext=m4a]/mp4',
                'outtmpl': filename,
            }
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([info['webpage_url']])
        except:
            print(f"\n\n    OPSS.... \n Houve Algum erro, Verifique sua URL ou sua Conexão a Internet e Tente Novamente!\n")
    else:
        print("\n\nEste tipo de arquivo não é suportada!\n")
else:
    print("\n\nA URL Informada é Invalida!\n")