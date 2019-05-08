# Echo client program
import socket
import sys

import random
import time
from tkinter import *

def close_window ():
    root.destroy()

def socket_comm():
    HOST = '169.254.140.239'    # The remote host
    PORT = 50007        # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)
            event = data.decode('utf-8')
            listbox.insert(END,event)
            listbox.pack()
            root.update_idletasks()
            root.update()
            time.sleep(0.2)
            # print(direction)

root = Tk()
root.minsize(200,300)
label = Label(root,text='Joystick GUI')
label.pack()

root.config(bg='gray')
listbox = Listbox(root, bg = "gray")
listbox.pack()

startbutton = Button(root, fg = "blue", text = 'Start',  width=15, height=1, command = socket_comm)
startbutton.pack(side = LEFT)

stopbutton = Button(root, fg = "blue", text = 'Quit',  width=15, height=1, command = close_window)
stopbutton.pack(side = RIGHT)

root.mainloop()
