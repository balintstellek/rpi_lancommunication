# Echo server program
import socket
import random
import time
# from sense_hat import SenseHat
# from time import sleep

# sense = SenseHat()

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
directions = ["up", "down", "left", "right", "middle"]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # event = sense.stick.wait_for_event()
            while True:
                event = random.choice(directions)
                conn.send(event.encode())
                time.sleep(2)
