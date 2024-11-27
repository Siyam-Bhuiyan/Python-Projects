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
        self.label=tk.Label(text="00:00:00", font=("Arial",20))
        self.label.pack()
        self.recording = False
        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.button.config(fg="black")
        else:
            self.recording = True
            self.button.config(fg="red")
            threading.Thread(target=self.record).start()

    def record(self):
        andro = pyaudio.PyAudio()
        stream=andro.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

        frames = []

        start= time.time()

        while self.recording:
            data= stream.read(1024)
            frames.append(data)

            passed = time.time() - start
            secs = int(passed % 60)
            mins = int((passed // 60) % 60)
            hours = int(passed // 3600)
            self.label.config(text=f"{hours:02d}:{mins:02d}:{secs:02d}")
            self.label.update()

        stream.stop_stream()
        stream.close()
        andro.terminate()

        i = 1
        while os.path.exists(f"recording{i}.wav"):
            i += 1

        sound_files = wave.open(f"recording{i}.wav", 'wb')
        sound_files.setnchannels(1)
        sound_files.setsampwidth(andro.get_sample_size(pyaudio.paInt16))
        sound_files.setframerate(44100)
        sound_files.writeframes(b"".join(frames))
        sound_files.close()


VoiceRecorder()

    

