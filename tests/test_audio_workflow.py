from audio_converter import mp3_to_wav
from audio_stegano_utils import embed_text_in_audio, extract_text_from_audio
import tempfile
import os

def test_audio_steganography_workflow():
    secret_message = "This is a secret test message"
    input_mp3 = "assets/sample_audio.mp3"
    
    # Use a permanent folder instead of temp
    output_dir = "assets"  # or a new folder like "output"
    os.makedirs(output_dir, exist_ok=True)
    
    wav_path = os.path.join(output_dir, "original.wav")
    stego_wav_path = os.path.join(output_dir, "stego.wav")

    mp3_to_wav(input_mp3, wav_path)
    embed_text_in_audio(wav_path, stego_wav_path, secret_message)
    extracted_message = extract_text_from_audio(stego_wav_path)

    assert extracted_message == secret_message, "Extracted message does not match original"

    print(f"Stego WAV saved at: {stego_wav_path}")
