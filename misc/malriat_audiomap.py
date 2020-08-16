#from playsound import playsound
import wave, struct, math

#def playtrack():
#    playsound("c:\\Users\\Jonah\\Desktop\\shortpiano.wav")

def read_wav():
    reader = wave.open("c:\\Users\\Jonah\\Desktop\\shortpiano.wav", "r")

    print( "Number of channels", reader.getnchannels())
    # 1 is mono, 2 is stereo.

    print( "Sample width", reader.getsampwidth())
    # The data of a WAV file is given as a sequence of frames. 
    # A frame consists of samples. There is one sample per channel, per frame. 
    # Every wav file has a sample width, or, the number of bytes per sample. 
    # Typically this is either 1 or 2 bytes.

    print( "Frame rate.", reader.getframerate())
    # Number of frames per second. Commonly 44.1khz/s or 44100hz/s

    print("Number of frames", reader.getnframes())
    # Seconds x frames per second = number of frames.

    print( "parameters:", reader.getparams())
    # Prints channels, sampwidth, framerate, numframes, compressiontype, and compression name.

    decoded = struct.unpack("<hh", reader.readframes(1))
    print(decoded)

def main():
    read_wav()

if __name__ == "__main__":
    main()