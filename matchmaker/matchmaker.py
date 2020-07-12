from tkinter import *
import random as rd 
import time

root = Tk()
root.resizable(width=False,height=False)
root.title("sahil's Matchmaker")

def show(x,y):
    global first
    global previousx ,previousy
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()
    if first: #checking for the first card
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy != y: #checking whetet the same card is not pressed again
        if buttons[previousx, previousy]['text'] != buttons[x, y]['text']: #checking if teext on both the buttons are same or not
            time.sleep(0.5)
            buttons[previousx, previousy]['text'] = ' '
            buttons[x, y]['text'] = ' '
        else:
            buttons[previousx, previousy]['command'] = DISABLED #if same then disable the button
            buttons[previousx , previousy]['bg'] = "white"
            buttons[x , y]['bg'] = "white"
            buttons[x, y]['command'] = DISABLED
            buttons[previousx, previousy]['fg'] = "red"
            buttons[x, y]['fg'] = "red"
        first = True

    

first = True
previousx = 0
previousy = 0
buttons = {} #for storing buttons
button_symbols = {} #for storing the symbols of the buttons
symbols = [u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
           u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728',
           u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
           u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728']

rd.shuffle(symbols)#shuffling all the symbols

#creating the buttons 
for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show(x, y), height=6, width=8,font="lucida 14 bold",fg="green",bg="black")
        button.grid(row=y,column=x)
        buttons[x, y] = button #addding the button to the buttons
        button_symbols[x, y] = symbols.pop() #adding symbols to the this

root.mainloop()
