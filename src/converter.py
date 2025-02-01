import pytesseract
import pyautogui
from PIL import Image
import get_screen

def image_convert(cordinate: dict) -> str:
    x, y, width, height = cordinate

    pyautogui.screenshot().save("iyakah.png")
    image = Image.open("iyakah.png").crop((x, y, x + width, y + height))

    return pytesseract.image_to_string(image)

