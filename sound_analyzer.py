import sounddevice as sd
import numpy as np

def analyze_sound():
    duration = 0.5
    fs = 44100

    print("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    spectrum = np.abs(np.fft.fft(audio[:, 0]))
    energy = np.mean(spectrum)

    if energy > 2500:
        return "Malauhog (Hard)"
    elif energy > 1500:
        return "Malakatad (Medium)"
    else:
        return "Malakanin (Soft)"
