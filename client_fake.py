import random
import time
from tkinter import *

def close_window ():
    root.destroy()

def socket_comm():
    directions = ["up", "down", "left", "right", "middle"]
    while True:
            event = random.choice(directions)
            time.sleep(2)
            dirs.set(event)
            root.update_idletasks()
            root.update()
            time.sleep(0.2)

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)

root.minsize(500,500)
label = Label(root,text='Joystick GUI')
label.config(width=100)
label.place(x=250, y=100, anchor="center")
label.pack()

root.config(bg='gray')
dirs = StringVar()
label2 = Label(root,textvariable=dirs)
label2.config(width=200, font=("Courier", 44))
label2.place(x=250, y=250, anchor="center")
dirs.set("Direction")


startbutton = Button(root, fg = "blue", text = 'Start',  width=15, height=1, command = socket_comm)
startbutton.place( x=200, y=400, anchor=SE)

stopbutton = Button(root, fg = "blue", text = 'Quit',  width=15, height=1, command = close_window)
stopbutton.place( x=300, y=400, anchor=SW)

root.mainloop()
