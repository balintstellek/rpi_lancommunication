import random
import time
from tkinter import *

root = Tk()
root.minsize(200,300)
label = Label(root,text='Joystick GUI')
label.pack()

root.config(bg='gray')
listbox = Listbox(root, bg = "gray")
listbox.pack()


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

directions = ["up", "down", "left", "right", "middle"]
while True:
            event = random.choice(directions)
            time.sleep(2)
            listbox.insert(END,event)
            listbox.pack()
            root.update_idletasks()
            root.update()
            print(event)
root.mainloop()
