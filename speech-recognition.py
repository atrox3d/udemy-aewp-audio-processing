from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment

notiziario = AudioSegment.from_mp3('notiziario.mp3')
notiziario.export('notiziario.wav', format='wav')
recognizer = Recognizer()

with AudioFile('notiziario.wav') as audio_file:
    audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio, language='it-IT')
print(text)
