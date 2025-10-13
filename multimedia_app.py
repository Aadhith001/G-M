import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from playsound import playsound
import cv2
import threading

# Function to play audio
def play_audio():
    playsound('sample_audio.mp3')  # Replace with your audio file

# Function to play video
def play_video():
    cap = cv2.VideoCapture('sample_video.mp4')  # Replace with your video file
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Function to load and display image
def load_image():
    img = Image.open('sample_image.jpg')  # Replace with your image file
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    panel.configure(image=img_tk)
    panel.image = img_tk

# GUI Setup
window = tk.Tk()
window.title("Multimedia App")

# Buttons
btn_img = tk.Button(window, text="Show Image", command=load_image)
btn_audio = tk.Button(window, text="Play Audio", command=lambda: threading.Thread(target=play_audio).start())
btn_video = tk.Button(window, text="Play Video", command=lambda: threading.Thread(target=play_video).start())

# Image display panel
panel = tk.Label(window)
panel.pack()

# Pack buttons
btn_img.pack(pady=5)
btn_audio.pack(pady=5)
btn_video.pack(pady=5)

# Start the GUI loop
window.mainloop()
