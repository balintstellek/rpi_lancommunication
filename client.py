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
            dirs.set(event)
            root.update_idletasks()
            root.update()
            time.sleep(0.2)
            # print(direction)

root = Tk()
root.geometry("500x300")
root.resizable(0, 0)

root.minsize(500,300)
label = Label(root,text='Joystick GUI',bg = "gray")
label.config(width=100,  height=2, font=("Courier", 24, "bold"))
label.place(x=250, y=100, anchor="center")
label.pack()

root.config(bg='gray')
dirs = StringVar()
label2 = Label(root, textvariable=dirs, bg = "gray", borderwidth=2, relief="groove", width = 200)
label2.config(width=10, font=("Courier", 44))
label2.place(x=250, y=150, anchor="center")
dirs.set("Direction")


startbutton = Button(root, fg = "black", text = 'Start', bg = "gray", borderwidth=2, relief="raised", command = socket_comm)
startbutton.config(width=15, height=1, font=("Courier", 10, "bold"))
startbutton.place( x=200, y=270, anchor=SE)

stopbutton = Button(root, fg = "black", text = 'Quit', bg = "gray", borderwidth=2, relief="raised", command = close_window)
stopbutton.config(width=15, height=1, font=("Courier", 10, "bold"))
stopbutton.place( x=300, y=270, anchor=SW)

root.mainloop()
