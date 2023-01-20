from pydub import AudioSegment

# load audio samples
beat = AudioSegment.from_wav('beat.wav')
sax = AudioSegment.from_wav('sax.wav')

# print len in ms
print(f'{len(beat) = }, {len(sax) = }')

# duplicate beat
beat2 = beat * 2

# mix sax on beat2
mixed = beat2.overlay(sax, gain_during_overlay=-10)
mixed.export('out/mixed.wav', format='wav')
