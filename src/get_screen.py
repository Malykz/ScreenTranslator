import mouse
import time
import pyautogui
import keyboard
import pyautogui as pt
from PIL import Image
import pytesseract

def get_cordinat_by_key(key) :
    cordinat = {}

    while True :
        if keyboard.is_pressed(key) :
            x, y = pyautogui.position()
            cordinat.update({"x" : x, "y" : y})
            break

    return cordinat

def get_image_size() -> dict :
    c1 = get_cordinat_by_key("q")
    c2 = get_cordinat_by_key("e")
    print(c1, c2)
    return c1["x"], c1["y"], c2["x"] - c1["x"], c2["y"] - c1["y"]

            





      

