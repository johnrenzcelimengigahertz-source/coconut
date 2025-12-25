import sounddevice as sd
import numpy as np

def analyze_sound():
    duration = 0.5  # seconds
    fs = 44100

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    spectrum = np.abs(np.fft.fft(audio[:, 0]))
    energy = np.mean(spectrum)

    if energy > 2000:
        return "Malauhog (Hard)"
    elif energy > 1000:
        return "Malakatad (Medium)"
    else:
        return "Malakanin (Soft)"
