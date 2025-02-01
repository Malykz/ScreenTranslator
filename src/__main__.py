from gui import app, display_label
import get_screen
from copy import copy

if __name__ == "__main__" :
    cordinate = get_screen.get_image_size()
    cordinate_copy = copy(cordinate)
    display_label("ScreenTranslator By Upi", cordinate_copy)
    app.mainloop()
