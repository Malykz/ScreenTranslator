import customtkinter as ctk
from converter import image_convert
app = ctk.CTk()
app.title("Screen Translator Python")
app.geometry("400x300")

app.attributes("-topmost", True)

label = ctk.CTkLabel(app)
label.pack(pady=20)

def display_label(t, cordinate: dict) -> str:
    label.configure(text=t)
    app.after(1000, display_label, image_convert(cordinate), cordinate)
