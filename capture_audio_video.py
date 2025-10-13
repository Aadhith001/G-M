import cv2
import sounddevice as sd
from scipy.io.wavfile import write
import threading
import tkinter as tk

# Audio recording function
def record_audio():
    duration = 5  # seconds
    fs = 44100    # sampling rate
    print("Recording Audio...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # wait until recording is finished
    write('recorded_audio.wav', fs, audio)
    print("Audio recording saved.")

# Video capture function
def capture_video():
    cap = cv2.VideoCapture(0)
    print("Press 'q' to stop video.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Webcam Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# GUI Setup
window = tk.Tk()
window.title("Capture Audio and Video")

btn_audio = tk.Button(window, text="Record Audio", command=lambda: threading.Thread(target=record_audio).start())
btn_video = tk.Button(window, text="Start Webcam", command=lambda: threading.Thread(target=capture_video).start())

btn_audio.pack(pady=10)
btn_video.pack(pady=10)

window.mainloop()
