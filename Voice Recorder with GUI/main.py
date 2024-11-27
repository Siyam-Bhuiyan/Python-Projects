import os
import wave
import time
import threading
import tkinter as tk
import pyaudio


class VoiceRecorder:
    def __init__(self):
        self.root=tk.Tk()
        self.root.resizable(False, False)
        self.button=tk.Button(text="🎤",font=("Arial",120,"bold"),
        command=self.click_handler)

        self.button.pack()
        self.label=tk.Label(text="00:00:00")
        self.label.pack()
        self.recording = False
        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.root.config(fg="black")
        else:
            self.recording = True
            self.root.config(fg="red")

VoiceRecorder()

    

