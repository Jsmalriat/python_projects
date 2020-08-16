from pydub import AudioSegment

sound = AudioSegment.from_mp3("C:\\Users\\Jonah\\Desktop\\STE-010.mp3")
sound.export("C:\\Users\\Jonah\\Desktop\\shortpiano.wav", format="wav")
