import sounddevice as sd
import soundfile as sf
from tkinter import *

def voice_rec():
	fs = 48000

	# seconds
	duration = 5000
	myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
	sd.wait()

	# Save as FLAC file at correct sampling rate
	return sf.write('my_audio_file.flac', myrecording, fs)

master = TK()

Label(master, text=" Voice Recoder : ").grid(row=0, sticky=W, rowspan=5)

b = Button(master, text="Start", command=voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()