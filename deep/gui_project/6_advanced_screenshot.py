import time
import keyboard # pip3 install keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot) # when user press the key "F9", do it
# keyboard.add_hotkey("shift+option+s", screenshot) # when user press the key "shift + option + s", do it

keyboard.wait("esc") # until user press the key "esc", do it