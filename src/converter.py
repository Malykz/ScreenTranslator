import pytesseract
import pyautogui
from PIL import Image
import translate
import getScreen
import os
import info

def image_temp_location(filename) -> str :
    temp_location = os.path.join(info.file_script_location, "temp")
    image_location = os.path.join(temp_location, filename)

    return image_location

def image_convert(cordinate: dict) -> str:
    image_location = image_temp_location("iyakah.png")
    pyautogui.screenshot().save(image_location)

    try :
        x, y, width, height = cordinate
        image = Image.open(image_location).crop((x, y, x + width, y + height))

    except Exception:
        raise ValueError("Be sure you were pointing correctly.")
    
    sentance =  pytesseract.image_to_string(image)
    return translate.sentance(sentance)