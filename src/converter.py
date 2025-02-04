import pytesseract
import pyautogui
from PIL import Image
import translate
import getScreen
import os


def image_temp_location(filename) -> str :
    script_location = os.path.dirname(os.path.relpath(__file__))
    temp_location = os.path.join(script_location, "temp")
    image_location = os.path.join(temp_location, filename)

    return image_location

def image_convert(cordinate: dict) -> str:
    image_location = image_temp_location("iyakah.png")

    x, y, width, height = cordinate
    pyautogui.screenshot().save(image_location)

    try :
        image = Image.open(image_location).crop((x, y, x + width, y + height))

    except Exception:
        raise ValueError("Be sure you were pointing correctly.")
    
    sentance =  pytesseract.image_to_string(image)
    return translate.sentance(sentance)