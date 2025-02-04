from gui import app, display_label
import getScreen


if __name__ == "__main__" :
    
    cordinate = getScreen.get_image_size()

    display_label("ScreenTranslator By Upi", cordinate)
    app.mainloop()
