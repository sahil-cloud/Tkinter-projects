from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

file_size = 0

def startDownload(url):
    global file_size

    path = askdirectory()
    try:
        if path is None:
            return

        obj = YouTube(url)

    # print(obj.title)
    # print(obj.streams.filter(only_audio=True))
    # print(obj.streams.filter(res="720p"))
        a = obj.streams.first() 
        a.download(path)
    except Exception as e:
        print(e)
        print("some error occured")

# for i in a:
#     print(i)

# print(a.title)
# print((a.filesize))

#creating GUI
root = Tk()
root.geometry("500x500")
root.title("Sahil's Youtube downloader  ")
# root.iconbitmap("you.ico")
# photo 
file = PhotoImage(file="you.jpg")
headIcon = Label(root,Image=file)
headIcon.pack(side=TOP)
root.mainloop()