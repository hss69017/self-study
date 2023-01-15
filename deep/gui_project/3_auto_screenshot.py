import time
from PIL import ImageGrab # pip3 install Pillow

time.sleep(5) # waiting 5 sec: user preparing time

for i in range(1, 11): # save 10 images every 2 seconds
    img = ImageGrab.grab() # take current screen image
    img.save("image{}.png".format(i)) # save as file
    time.sleep(2) # every 2 seconds