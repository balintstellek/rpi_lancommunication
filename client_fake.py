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
            listbox.insert(END,event)
            listbox.pack()
            root.update_idletasks()
            root.update()
            print(event)

root = Tk()
root.minsize(200,300)
label = Label(root,text='Joystick GUI')
label.pack()

root.config(bg='gray')
listbox = Listbox(root, bg = "gray")
listbox.pack()

startbutton = Button(root, bg = "blue", text = 'Start',  width=15, height=1, command = socket_comm)
startbutton.pack(side = LEFT)

stopbutton = Button(root, bg = "blue", text = 'Quit',  width=15, height=1, command = close_window)
stopbutton.pack(side = RIGHT)

root.mainloop()
