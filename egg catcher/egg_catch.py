from tkinter import *
from random import randrange
from itertools import cycle
from tkinter import messagebox

canvas_width = 800
canvas_height = 500

root = Tk()
root.title("Sahil's Egg catcher")
#creating the main canvas body
c = Canvas(root,width = canvas_width,height=canvas_height,bg='deep sky blue')
c.create_rectangle(-5, canvas_height+5, canvas_width+5,canvas_height-100, fill='sea green', width=0)
c.create_oval(-80,-80,150,150,fill='orange',width=0)
c.pack()

#creating the catcher and eggs
color_cycle = cycle(['light blue', 'light green', 'light pink',
                     'light yellow','blue', 'black', 'white', 'green', 'pink', 'purple' ])

egg_width = 45
egg_height = 55
egg_speed = 500
egg_score = 10
egg_interval = 4000
difficulty_factor = 0.95

catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2,
                       start=200, extent=140, style='arc', outline=catcher_color, width=5)

score = 0
score_text = c.create_text(100,20,anchor='ne',font="Arial 12 bold",text="Score:"+str(score))

lives = 3
lives_text = c.create_text(canvas_width-80, 20, anchor='nw', font="Arial 14 bold", text="Lives:"+str(lives))

eggs = []

def create_eggs():
    x = randrange(35,780)
    y = 40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    root.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg, 0, 10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives == 0:
        messagebox.showinfo('GAME OVER!', 'Final Score : ' + str(score))
        root.destroy()


def lose_a_life():
    global lives
    lives -= 1
    c.itemconfigure(lives_text, text='Lives : ' + str(lives))

def catch_check():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, catch_check)


def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text, text='Score : ' + str(score))


def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)


def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)


c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.focus_set()

root.after(1000, create_eggs)
root.after(1000, move_eggs)
root.after(1000, catch_check)

root.mainloop()
