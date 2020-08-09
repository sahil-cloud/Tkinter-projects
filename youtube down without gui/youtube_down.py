from pytube import YouTube

url = 'https://www.youtube.com/watch?v=khJlrj3Y6Ls'

you = YouTube(url)
# print(you.streams.all())
# getting all the streams
allStreams = you.streams.all()
# for stream in you.streams.all():
#     print(stream)

print(allStreams[1])

allStreams[1].download('C:\\Users\\USER\\Desktop\\pytube videos')

