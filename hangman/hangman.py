from tkinter import *
import random
import tkinter.messagebox as tmsg

root = Tk()
root.title("Sahil's Hangman")
root.geometry("700x500")
root.resizable(width=False,height=False)
root.configure(bg='light sky blue')

validletters = "abcdefghijklmnopqrstuvwxyz"
x=5
y1=450
lives_r = 10
l1 = Label(root, text="Lives : "+str(lives_r),font="lucida 12 bold")
l1.place(x=600, y=100)


'''

the main logic and functions started 
'''

def Hangman():
    global word_with_spaces
    global no_guess
    no_guess = 0
    tmsg.showinfo("WELCOME TO HANGMAN!","  Press Ok to continue! Your game has been started")
    word = random.choice(["lassanmama", "kabirsingh", "baburav", "drstrange",
                          "mcbctoc", "herapheri", "avengers", "pornhub", "rambharose", "chutiya"])
    word_with_spaces = " ".join(word)
    the_word.set(" ".join("_"*len(word)))
    

     
    
'''

the main logic and functions ended
'''
guess = ''
def click(letter):
    global no_guess
    if no_guess <= 10:
        txt = list(word_with_spaces)
        guessed = list(the_word.get())
        if word_with_spaces.count(letter)>0:
            for i in range(len(txt)):
                if txt[i] == letter:
                    guessed[i] = letter
                the_word.set("".join(guessed))
                if the_word.get() == word_with_spaces:
                    messagebox.showinfo("HANGMAN SAYS!","YOU WON CONGO!")
        else:
            no_guess += 1
            if no_guess == 10:
                messagebox.showinfo("HANGMAN SAYS!", "GAME OVER!")




def file():
    global name
    nam1 = name.get()
    if nam1 == "":
        tmsg.showinfo("Hangman Says","Enter you name first")
    else:
        nam1 = "Welcome "+nam1
        list1.delete(0, END)
        list1.insert(END, nam1)
        Hangman()

for i in validletters:
    if i == 'n':
        y1 = 395
        x = 5
    b = Button(root, text=i, font="lucida 9 bold", width=5, height=2,command= lambda i=i:click(i))
    b.place(x=x,y=y1)
    x += 54
    
#creating name window
name = StringVar()
en = Entry(root,textvariable=name,width=20,font="lucida 15 bold")
en.place(x=20,y=40)
# t = Text(root,text="enter your name")
# t.place(x=20,y=20)
l = Label(root,text="Enter your name")
l.place(x=20,y=15)

b1 = Button(root,text="submit",command=file)
b1.place(x=260,y=42)

list1 = Listbox(root, width=50, height=4,font="lucida 10 bold")
list1.place(x=320,y=20)

l2 = Label(root, text="Guess the word",font="lucida 10 bold")
l2.place(x=100, y=215)

# list1 = Listbox(root, width=50, height=4, font="lucida 10 bold")
# list1.place(x=100, y=250)

the_word = StringVar()
# the_word.set("sahil")
l3 = Label(root, textvariable=the_word, font="lucida 20 bold")
l3.place(x=100, y=255)

b1 = Button(root, text="submit", command=file)
b1.place(x=260, y=42)

root.mainloop()
