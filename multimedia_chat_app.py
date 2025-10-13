import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import Image, ImageTk
from playsound import playsound
import threading

# Function to send text message
def send_text():
    msg = text_entry.get()
    if msg:
        chat_box.insert(tk.END, f"You: {msg}\n")
        text_entry.delete(0, tk.END)
        chat_box.yview(tk.END)

# Function to send image
def send_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if path:
        chat_box.insert(tk.END, f"You sent an image: {path}\n")
        img = Image.open(path)
        img.thumbnail((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        image_label = tk.Label(chat_frame, image=img_tk)
        image_label.image = img_tk
        image_label.pack()
        chat_box.yview(tk.END)

# Function to send audio
def send_audio():
    path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if path:
        chat_box.insert(tk.END, f"You sent an audio message: {path}\n")
        threading.Thread(target=lambda: playsound(path)).start()
        chat_box.yview(tk.END)

# GUI Setup
window = tk.Tk()
window.title("Multimedia Messaging App")
window.geometry("400x500")

# Chat display frame
chat_frame = tk.Frame(window)
chat_box = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=20)
chat_box.pack()
chat_frame.pack(pady=10)

# Entry for text input
text_entry = tk.Entry(window, width=30)
text_entry.pack(side=tk.LEFT, padx=5)

# Buttons
btn_text = tk.Button(window, text="Send Text", command=send_text)
btn_image = tk.Button(window, text="Send Image", command=send_image)
btn_audio = tk.Button(window, text="Send Audio", command=send_audio)

btn_text.pack(side=tk.LEFT)
btn_image.pack(side=tk.LEFT)
btn_audio.pack(side=tk.LEFT)

window.mainloop()
