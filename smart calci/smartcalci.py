from tkinter import *

root = Tk()
root.geometry("550x450")
root.resizable(width=False,height=False)
root.title("Sahil's Smart Calculator")
root.config(bg='lightgreen')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    L = a if a > b else b
    while L <= a*b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


def extract(text1):
    l = []
    for t in text1.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def calculate():
    text = text1.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract(text)
                r = operations[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0, END)
                list.insert(END, 'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')




operations = {
    'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
    'SUB': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
    'LCM': lcm, 'HCF': hcf, 'PRODUCT': mul, 'MULTIPLICATION': mul,
    'MULTIPLY': mul, 'DIVISION': div, 'DIV': div, 'DIVIDE': div, 'MOD': mod,
    'REMANDER': mod, 'MODULUS': mod,
    'JODO':add,'GHTAO':sub,'GUNA':mul,'BHAAG':div,'BHAG':div,'+':add,'-':sub,'*':mul,'/':div,
} 



l1 = Label(root,text='I am Smart Calculator',width=20,padx=3)
l1.place(x=200,y=10)
l2 = Label(root, text='How can I help you?', width=20, padx=3)
l2.place(x=200, y=150)

text1 = StringVar()
e = Entry(root, width=50, textvariable=text1)
e.pack(ipadx=5,ipady=8,pady=180)


b1 = Button(root, text='Just this', command=calculate)
b1.place(x=260, y=230)

list = Listbox(root, width=40, height=3)
list.place(x=170, y=270)
root.mainloop()
