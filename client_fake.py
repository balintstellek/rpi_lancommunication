import random
import time

directions = ["up", "down", "left", "right", "middle"]
while True:
            event = random.choice(directions)
            time.sleep(2)
            print(event)
