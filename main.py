"""
RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work

solution:

- goto https://www.gyan.dev/ffmpeg/builds/
- download ffmpeg*essentials*.zip
- unzip the contents of the bin subfolder inside venv/Scripts (where python.exe is)
"""
from pydub import AudioSegment

# load audio file
original = AudioSegment.from_wav('beat.wav')
print(f'{type(original)=}, {original=}')

# reverse audiofile
reversed = original.reverse()
reversed.export('out/reversed.wav')

# get clip of audiofile
# slicing in milliseconds! how cool is that?
first_2_minutes = original[0:2000]
first_2_minutes.export('out/first_2_minutes.wav')

# get len of audio in milliseconds
print(f'{len(original)=} ms')
print(f'{len(reversed)=} ms')
print(f'{len(first_2_minutes)=} ms')

# append reversed to original
merged = original + reversed
merged.export('out/merged.wav')
print(f'{len(merged)=} ms')

# create 1000 ms of silence
silence = AudioSegment.silent(1000)
silence.export('out/silence.wav')
print(f'{len(silence)=} ms')

# repeat clip n times
double_original = original * 2
double_original.export('out/double_original.wav')
print(f'{len(double_original)=} ms')

# increase volume by 15 DB
double_original_increased = double_original + 15

doubleoriginalincreased_silence_reversed = double_original_increased + silence + reversed
doubleoriginalincreased_silence_reversed.export('out/doubleoriginalincreased-silence-reversed.wav')
print(f'{len(doubleoriginalincreased_silence_reversed)=} ms')

