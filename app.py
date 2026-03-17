import customtkinter as ctk
from tkinter import filedialog, messagebox
from encrypt import encrypt_image
from decrypt import decrypt_image
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

image_path = ""

def select_file():
    global image_path
    image_path = filedialog.askopenfilename()

    if image_path:
        file_label.configure(text=image_path.split("/")[-1])


def encrypt():

    if image_path == "":
        messagebox.showerror("Error", "Please select an image first")
        return

    x0 = float(x0_entry.get())
    r = float(r_entry.get())

    status_label.configure(text="Encrypting... running")

    def process():
        encrypt_image(image_path, x0, r)

        status_label.configure(text="Ready")

        messagebox.showinfo("Success", "Encryption completed successfully!")

    threading.Thread(target=process).start()


def decrypt():

    x0 = float(x0_entry.get())
    r = float(r_entry.get())

    status_label.configure(text="Decrypting... running")

    def process():
        decrypt_image("encrypted.png", x0, r)

        status_label.configure(text="Ready")

        messagebox.showinfo("Success", "Decryption completed successfully!")

    threading.Thread(target=process).start()


app = ctk.CTk()
app.geometry("520x400")
app.title("Chaotic Image Encryption System")

title = ctk.CTkLabel(
    app,
    text="Chaotic Image Encryption",
    font=("Arial", 28, "bold")
)
title.pack(pady=25)

select_btn = ctk.CTkButton(
    app,
    text="Select Image",
    command=select_file,
    fg_color="#2ecc71",
    hover_color="#27ae60",
    width=220,
    height=40
)
select_btn.pack()

file_label = ctk.CTkLabel(app, text="No file selected")
file_label.pack(pady=10)

frame = ctk.CTkFrame(app)
frame.pack(pady=15)

x0_label = ctk.CTkLabel(frame, text="Initial Key (x0)")
x0_label.grid(row=0, column=0, padx=15, pady=15)

x0_entry = ctk.CTkEntry(frame, width=120)
x0_entry.insert(0, "0.5")
x0_entry.grid(row=0, column=1)

r_label = ctk.CTkLabel(frame, text="Control Parameter (r)")
r_label.grid(row=1, column=0, padx=15, pady=15)

r_entry = ctk.CTkEntry(frame, width=120)
r_entry.insert(0, "3.9")
r_entry.grid(row=1, column=1)

encrypt_btn = ctk.CTkButton(
    app,
    text="Encrypt Image",
    command=encrypt,
    fg_color="#e67e22",
    hover_color="#d35400",
    width=220,
    height=40
)
encrypt_btn.pack(pady=10)

decrypt_btn = ctk.CTkButton(
    app,
    text="Decrypt Image",
    command=decrypt,
    fg_color="#3498db",
    hover_color="#2980b9",
    width=220,
    height=40
)
decrypt_btn.pack(pady=10)

status_label = ctk.CTkLabel(
    app,
    text="Ready",
    font=("Arial", 14)
)
status_label.pack(pady=20)

app.mainloop()
