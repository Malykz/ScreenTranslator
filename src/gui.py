import customtkinter as ctk
from converter import image_convert
from copy import copy
import keyboard

app = ctk.CTk()
app.title("Screen Translator Python")
app.geometry("400x300")
app.attributes("-topmost", True)

label = ctk.CTkLabel(app)
label.pack(pady=20)

def display_label(t, cordinate: dict) -> str:

    label.configure(text=t, font=("Arial", 32), justify="left", width=30)
    teks = t

    if keyboard.is_pressed("t") :
        print("Hello World")
        teks = image_convert(cordinate)

    app.after(10, display_label, teks, cordinate) 
