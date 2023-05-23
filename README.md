# audio_convertor
This servise converts wave-audio to mp3-audio


pip install ffmpeg-downloader
ffdl install --add-path


это работает

 import pydub
 pydub.AudioSegment.converter = 'c:\\FFmpeg\\bin\\ffmpeg.exe'
 sound = pydub.AudioSegment.from_mp3("test.mp3")