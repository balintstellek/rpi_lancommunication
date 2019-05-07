# Echo server program
import socket
import random
# from sense_hat import SenseHat
# from time import sleep

# sense = SenseHat()

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # event = sense.stick.wait_for_event()
            while True:
                p = random.randint(1, 5)
                if p == 1:
                    event = "up"
                elif p = 2:
                    event = "down"
                elif p = 3:
                    event = "left"
                elif p = 4:
                    event = "right"
                else:
                    event = "middle"
                conn.send(event.direction.encode())
                sleep(5)
