from gui import app, display_label
import getScreen


if __name__ == "__main__" :

    print("Please set the corner left top with key 'q'\nand right bottom with key 'e'")
    cordinate = getScreen.get_image_size()

    display_label("ScreenTranslator By Upi", cordinate)
    app.mainloop()
