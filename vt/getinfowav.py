import wave

def getWaveInfo():
     w = wave.open('a08.wav','rb')
     print("Number of channels is: ",    w.getnchannels())
     print("Sample width in bytes is: ", w.getsampwidth())
     print("Framerate is: ",             w.getframerate())
     print("Number of frames is: ",      w.getnframes())

if __name__ == "__main__":
     getWaveInfo()