from pydub import AudioSegment

def mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")

def wav_to_mp3(wav_path, mp3_path):
    audio = AudioSegment.from_wav(wav_path)
    audio.export(mp3_path, format="mp3")
