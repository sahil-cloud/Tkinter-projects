from pytube import YouTube
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import PIL.Image
from tkinter.filedialog import *
from threading import *

file_size = 0

# for showing %


# def progress(stream=None, chunk=None, filehandle=None, bytes_remaining=None):
#     # file_size=a.filesize
#     global file_size
#     global obj

#     file_down =(file_size-bytes_remaining)
#     per = (file_down/file_size)*100
#     btn.config(text="{:00.0f} % downloaded".format(per))

# def startDownloadThread():
#     thread=Thread(target=startDownload)
#     thread.start()

def startDownload():
    global file_size
    btn.config(text="Please wait...")
    btn.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn1.config(state=DISABLED)

    # path = "C:\\Users\\USER\\Downloads"
    try:
        url = urlEntry.get()
        print(url)
        # btn.config(text="Please wait...")

        obj = YouTube(url)
        a = obj.streams.first()

        
        # print(url)
        title = Label(root, text="Title: "+obj.title, font="lucida 14")
        title.place(x=10, y=150)
        title1 = Label(root, text="file size: " +
                    str(a.filesize/1000000)+" MB", font="lucida 14")
        title1.place(x=10, y=200)
        title2 = Label(root, text="length: " +
                    str(obj.length/60)+" min", font="lucida 14")
        title2.place(x=10, y=250)
        title3 = Label(root, text="rating: "+str(obj.rating), font="lucida 14")
        title3.place(x=10, y=300)
        title4 = Label(root, text="views: "+str(obj.views), font="lucida 14")
        title4.place(x=10, y=350)

        btn.config(text="downloading")


        path = askdirectory()

        if path is None:
            exit()
    # print(obj.title)
    # print(obj.streams.filter(only_audio=True))
    # print(obj.streams.filter(res="720p"))
        file_size = a.filesize
        

        print(file_size)
        print(path)
        a.download(path)
        messagebox.showinfo("Download finished","downloaded successfully")
        btn.config(text="download 720p")
        btn.config(state=NORMAL)
        btn1.config(state=NORMAL)
        btn2.config(state=NORMAL)
        urlEntry.delete(0,END)
        title.place_forget()
        title1.place_forget()
        title2.place_forget()
        title3.place_forget()
        title4.place_forget()
    except Exception as e:
        print(e)
        print("some error occured")
        exit


def startDownload1():
    global file_size
    btn1.config(text="Please wait...")
    btn.config(state=DISABLED)
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)

    # path = "C:\\Users\\USER\\Downloads"
    try:
        url = urlEntry.get()
        print(url)
        

        

        obj = YouTube(url)

    # print(obj.title)
    # print(obj.streams.filter(only_audio=True))
    # print(obj.streams.filter(res="720p"))
        a = obj.streams.filter(res='360p',subtype='mp4')
        file_size = a.filesize
        title = Label(root, text="Title: "+obj.title, font="lucida 14")
        title.place(x=10, y=150)
        title1 = Label(root, text="file size: " +
                       str(a.filesize/1000000)+" MB", font="lucida 14")
        title1.place(x=10, y=200)
        title2 = Label(root, text="length: " +
                       str(obj.length/60)+" min", font="lucida 14")
        title2.place(x=10, y=250)
        title3 = Label(root, text="rating: "+str(obj.rating), font="lucida 14")
        title3.place(x=10, y=300)
        title4 = Label(root, text="views: "+str(obj.views), font="lucida 14")
        title4.place(x=10, y=350)

        btn1.config(text="downloading")
        path = askdirectory()
        if path is None:
            return


        print(file_size)
        print(path)
        a.download(path)
        btn.config(text="Started downloading")
        btn.config(state=NORMAL)
        messagebox.showinfo("Download finished", "downloaded successfully")
        urlEntry.delete(0, END)
        title.place_forget()
        title1.place_forget()
        title2.place_forget()
        title3.place_forget()
        title4.place_forget()
    except Exception as e:
        print(e)
        print("some error occured")
        exit


def startDownload2():
    global file_size
    btn2.config(text="Please wait...")
    btn.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn1.config(state=DISABLED)

    # path = "C:\\Users\\USER\\Downloads"
    try:
        url = urlEntry.get()
        print(url)
        # btn.config(text="Please wait...")

        obj = YouTube(url)
        a = obj.streams.filter(only_audio=True)

        # print(url)
        title = Label(root, text="Title: "+obj.title, font="lucida 14")
        title.place(x=10, y=150)
        title1 = Label(root, text="file size: " +
                       str(a.filesize/1000000)+" MB", font="lucida 14")
        title1.place(x=10, y=200)
        title2 = Label(root, text="length: " +
                       str(obj.length/60)+" min", font="lucida 14")
        title2.place(x=10, y=250)
        title3 = Label(root, text="rating: "+str(obj.rating), font="lucida 14")
        title3.place(x=10, y=300)
        title4 = Label(root, text="views: "+str(obj.views), font="lucida 14")
        title4.place(x=10, y=350)

        btn2.config(text="downloading")

        path = askdirectory()

        if path is None:
            exit()
    # print(obj.title)
    # print(obj.streams.filter(only_audio=True))
    # print(obj.streams.filter(res="720p"))
        file_size = a.filesize

        print(file_size)
        print(path)
        a.download(path)
        messagebox.showinfo("Download finished", "downloaded successfully")
        btn2.config(text="download 720p")
        btn.config(state=NORMAL)
        btn1.config(state=NORMAL)
        btn2.config(state=NORMAL)
        urlEntry.delete(0, END)
        title.place_forget()
        title1.place_forget()
        title2.place_forget()
        title3.place_forget()
        title4.place_forget()
    except Exception as e:
        print(e)
        print("some error occured")
        exit

#creating GUI
root = Tk()
root.geometry("500x500")
root.title("Sahil's Youtube downloader  ")
# root.iconbitmap("you.ico")
# photo 
# img = ImageTk.PhotoImage(PIL.Image.open("you.jpg").convert("RGB"))
# img = tk.PhotoImage(file="./gif.gif")
# headIcon = Label(root,Image=img)
# headIcon.pack(side=TOP)
Label(text="Youtube downloader",font=("lucida 15 bold")).pack(side=TOP,pady=3)

# url entery
font = ("Helvetica", 15, "bold")
urlEntry = Entry(root, font=font,justify=CENTER)
urlEntry.pack(fill=X, pady=20,padx=10)

urlEntry.insert(0, "Enter URL")
urlEntry.configure(state=DISABLED)


def on_click(event):
    urlEntry.configure(state=NORMAL)
    urlEntry.delete(0, END)

    # make the callback only work once
    urlEntry.unbind('<Button-1>', on_click_id)


on_click_id = urlEntry.bind('<Button-1>', on_click)

# download buton
btn = Button(root,text="Download 720p",font="lucida 12",relief=RIDGE,command=startDownload)
btn.place(x=60,y=100)

btn1 = Button(root,text="Download 360p",font="lucida 12",relief=RIDGE,command=startDownload1)
btn1.place(x=200,y=100)

btn2 = Button(root, text="Download audio", font="lucida 12",relief=RIDGE, command=startDownload2)
btn2.place(x=340,y=100)

# labelling
# vdesc = Label(root,text="video desc",font="lucida 15")
# vdesc.pack(side=TOP)

root.mainloop()
