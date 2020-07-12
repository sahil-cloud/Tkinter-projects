from pytube import YouTube

url = "https://www.youtube.com/watch?v=ID2A8_CpmG4"
obj = YouTube(url)

a = obj.streams.first()
path = "C://Users//User//Desktop"

a.download(path)
