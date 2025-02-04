import pytesseract
import pyautogui
from PIL import Image
import translate
import getScreen

def image_convert(cordinate: dict) -> str:
    x, y, width, height = cordinate
    pyautogui.screenshot().save("iyakah.png")

    try :
        image = Image.open("iyakah.png").crop((x, y, x + width, y + height))

    except Exception:
        raise ValueError("Be sure you were pointing correctly.")
    
    sentance =  pytesseract.image_to_string(image)
    return translate.sentance(sentance)