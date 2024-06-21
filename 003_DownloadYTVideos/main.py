from pytube import YouTube

def download_video_yt(url, path='D:\\alang\\Videos'):
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(output_path=path)
        print("Descarga completada")
    except Exception as e:
        print("Error al descargar:", e)

url_youtube = input("Pega la URL del video de YT: ")
download_video_yt(url_youtube)

