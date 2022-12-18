from tkinter import *

from math import *


def getvals(event):
    value = event.widget.cget('text')
    if value == 'clr':
        sc_variable.set(' ')
    elif value == '=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception:
            sc_variable.set('Error!!!!press clr')
    else:
        sc_variable.set(f'{sc_variable.get()}{value}')


window = Tk()
window.geometry('530x500')
window.resizable(width=False,height=False)
window.title('Project_2__p-10')

sc_variable = StringVar()
screen = Entry(window, textvariable=sc_variable, font='lucida 35 bold', fg='gray', bg='white', borderwidth=10)
screen.pack(pady=30)

f1 = Frame(window)
f1.pack()
b1 = Button(f1, text='7', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b2 = Button(f1, text='8', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b3 = Button(f1, text='9', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b4 = Button(f1, text='*', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='blue', width=3)
b5 = Button(f1, text='sin', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue',width=3)
b6 = Button(f1, text='(', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
b6.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5, b6]
for i in range(6): buttons[i].grid(row=4, column=i)

f2 = Frame(window)
f2.pack()
b1 = Button(f2, text='4', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b2 = Button(f2, text='5', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b3 = Button(f2, text='6', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b4 = Button(f2, text='-', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='blue', width=3)
b5 = Button(f2, text='cos', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue',width=3)
b6 = Button(f2, text=')', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
b6.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5, b6]
for i in range(6): buttons[i].grid(row=4, column=i)

f3 = Frame(window)
f3.pack()
b1 = Button(f3, text='1', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b2 = Button(f3, text='2', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b3 = Button(f3, text='3', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b4 = Button(f3, text='+', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='blue', width=3)
b5 = Button(f3, text='tan', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue',width=3)
b6 = Button(f3, text='%', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
b6.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5, b6]
for i in range(6): buttons[i].grid(row=4, column=i)

f4 = Frame(window)
f4.pack()
b1 = Button(f4, text='=', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='green', width=3)
b2 = Button(f4, text='0', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='red', bg='pink', width=3)
b3 = Button(f4, text='clr', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='red', width=3)
b4 = Button(f4, text='/', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='blue', width=3)
b5 = Button(f4, text='pi', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b6 = Button(f4, text='.', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
b6.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5, b6]
for i in range(6): buttons[i].grid(row=4, column=i)

window.mainloop()
