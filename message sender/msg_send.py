import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'sp4HFuKAI9EqrVdvLX08jgSDtYxa27knZPhyzl3bfR1oOJUW5CXbDqmZ5ueoi7pRjSLl1FG0Cdg6wTkW',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    # print(num)
    # print(msg)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


# Creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)

textNumber.insert(0, "Enter number")
textNumber.configure(state=DISABLED)


def on_click(event):
    textNumber.configure(state=NORMAL)
    textNumber.delete(0, END)

    # make the callback only work once
    textNumber.unbind('<Button-1>', on_click_id)


on_click_id = textNumber.bind('<Button-1>', on_click)

textMsg = Text(root)
textMsg.pack(fill=X)

# textMsg.insert(0, "Enter message")
# textMsg.configure(state=DISABLED)


# def on_click(event):
#     textMsg.configure(state=NORMAL)
#     textMsg.delete(0, END)

#     # make the callback only work once
#     textMsg.unbind('<Button-1>', on_click_id)


# on_click_id = textMsg.bind('<Button-1>', on_click)

sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()
