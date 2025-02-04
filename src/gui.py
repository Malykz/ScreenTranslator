import customtkinter as ctk
from converter import image_convert
from copy import copy
import keyboard
from options import options

app = ctk.CTk()
app.title("Screen Translator Python")
app.geometry(f"{options.displayWidth}x{options.displayHeight}")
app.attributes("-topmost", True)

label = ctk.CTkLabel(app)
label.pack(pady=2)

def display_label(t, cordinate: dict) -> str:
    label.configure(text=t, font=("Arial", int(options.fontSize)), justify="left", width=30)
    teks = t

    if keyboard.is_pressed(options.key) :
        print("Hello World")
        teks = image_convert(cordinate)

    app.after(10, display_label, teks, cordinate) 
