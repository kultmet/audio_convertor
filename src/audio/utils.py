from fastapi import File, UploadFile
from pydub import AudioSegment
from pydub.playback import play
import os

from constants import MEDIA_ROOT, FFMPEG_PATH


def wav_to_mp3(wav_file: UploadFile):
    """Saves WAV audio file, next Converts to MP3 audio and next remove WAV audio file."""
    filepath = f'{MEDIA_ROOT}/{wav_file.filename}'
    with open(filepath, 'wb') as file:
        file.write(wav_file.file.read())
    AudioSegment.converter = FFMPEG_PATH
    song = AudioSegment.from_wav(filepath)
    filename, _ = os.path.splitext(wav_file.filename)
    song.export(f'{MEDIA_ROOT}/{filename}.mp3', format='mp3')
    os.remove(filepath)
