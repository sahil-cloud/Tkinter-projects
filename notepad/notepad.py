from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root =Tk()
#code 

def basic_setup():
    root.title("Untitled - Notepad")
    root.minsize(250,200)
    # root.configure(background="red")
    # root.wm_iconbitmap("C:\python\TKINTER\2.ico")

#creating text field area and adding scrool bars
file = None
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scroll.set)
text.pack(fill=BOTH)

scroll.config(command=text.yview)


#menu functions
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0,END) # for delete the text field

def openfile():
    global file 
    file = askopenfilename(
    filetypes=[("All Files","*.*"),("Text  Documents","*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        text.delete(1.0,END)
        f=open(file,"r+")
        text.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(
            filetypes=[("All Files", "*.*"), ("Text  Documents", "*.txt")])

        if file == "":
            file = None
        else:
            # saving new file
            f = open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")

    else:
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()


def quitApp():
    root.destroy()

def cutfile():
    text.event_generate(("<<Cut>>"))

def copyfile():
    text.event_generate(("<<Copy>>"))


def pastefile():
    text.event_generate(("<<Paste>>"))


def selectall():
    text.tag_add(SEL,"1.0",END)
    text.mark_set(INSERT,"1.0")
    text.see(INSERT)
    return 'break'

def help():
    tmsg.showinfo("NEED HELP!", "If you need any help CONTACT ME at sahiljasuja666@gmail.com")

def rate():
    value = tmsg.askquestion("How Was Your Experience",
                          "WAS IT GOOD! For any improvement CONTACT ME at sahiljasuja666@gmail.com")

    if value == "yes":
        msg = "Thank You For Your Feedback"
    else:
        msg = "Tell me what went wrong, CONTACT ME at sahiljasuja666@gmail.com"
    tmsg.showinfo("Experience",msg)
def menu_setup():
    mainmenu = Menu(root) #main menu
    
    #creating sub menus
    m1 = Menu(mainmenu,tearoff=0)
    m1.add_command(label="New",command=newfile)
    m1.add_command(label="Open", command=openfile)
    m1.add_command(label="Save",command=savefile)
    m1.add_separator()
    m1.add_command(label="Exit", command=quitApp)

    #configure the menu
    root.config(menu=mainmenu)

    #adding to themainmenu
    mainmenu.add_cascade(label="File",menu=m1)

    #creating sub menus
    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label="Cut", command=cutfile)
    m2.add_command(label="Copy", command=copyfile)
    m2.add_command(label="Paste", command=pastefile)
    m2.add_separator()
    m2.add_command(label="Select All", command=selectall)

    #configure the menu
    root.config(menu=mainmenu)

    #adding to themainmenu
    mainmenu.add_cascade(label="Edit", menu=m2)

   #creating sub menus
    # m3 = Menu(mainmenu, tearoff=0)
    # m3.add_command(label="Light Theme", command=light)
    # m3.add_separator()
    # m3.add_command(label="Dark Theme", command=dark)

    # #configure the menu
    # root.config(menu=mainmenu)

    # #adding to themainmenu
    # mainmenu.add_cascade(label="Theme", menu=m3)

    #creating view
    # m5 = Menu(mainmenu, tearoff=0)
    # m5.add_command(label="Status Bar", command=status_bar)
    #configure the menu
    # root.config(menu=mainmenu)

    # #adding to themainmenu
    # mainmenu.add_cascade(label="View", menu=m5)

    #creating sub menus
    m4 = Menu(mainmenu, tearoff=0)
    m4.add_command(label="Help", command=help)
    m4.add_separator()
    m4.add_command(label="Rate Us", command=rate)

    #configure the menu
    root.config(menu=mainmenu)

    #adding to themainmenu
    mainmenu.add_cascade(label="Help", menu=m4)

#creating status bar at the bottom
def status_bar():
    statusvar = StringVar()
    statusvar.set("Created By SAHIL JASUJA")
    sbar = Label(root,textvariable=statusvar,relief=SUNKEN,font=("cursive",10,"bold"),anchor="e",background="darkolivegreen")
    sbar.pack(side=BOTTOM,fill=X)

#creating scrollbars
# def scroll_bar():


#functions calling
basic_setup()
menu_setup()
status_bar()
# scroll_bar()

#code ends here
root.mainloop()
