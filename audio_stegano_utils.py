import wave

def text_to_binary(message):
    """Convert text message to binary string."""
    return ''.join(format(ord(c), '08b') for c in message)

def binary_to_text(binary_str):
    """Convert binary string back to text."""
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(b, 2)) for b in chars if int(b, 2) != 0)

def embed_text_in_audio(input_audio_path, output_audio_path, message):
    """
    Embed text message into audio file by modifying LSB of audio frames.
    """
    with wave.open(input_audio_path, 'rb') as audio:
        params = audio.getparams()
        frames = bytearray(audio.readframes(params.nframes))

    binary_message = text_to_binary(message) + '1111111111111110'  # EOF marker

    if len(binary_message) > len(frames):
        raise ValueError("Message too long to hide in this audio.")

    for i in range(len(binary_message)):
        frames[i] = (frames[i] & 0xFE) | int(binary_message[i])

    with wave.open(output_audio_path, 'wb') as stego_audio:
        stego_audio.setparams(params)
        stego_audio.writeframes(frames)

def extract_text_from_audio(stego_audio_path):
    """
    Extract hidden text message from stego audio by reading LSBs.
    Returns the hidden text or raises ValueError if no valid message found.
    """
    with wave.open(stego_audio_path, 'rb') as audio:
        frames = bytearray(audio.readframes(audio.getnframes()))

    binary_data = ''.join(str(byte & 1) for byte in frames)

    eof_marker = '1111111111111110'
    end_index = binary_data.find(eof_marker)

    if end_index == -1:
        raise ValueError("No hidden message found.")

    hidden_binary = binary_data[:end_index]
    hidden_text = binary_to_text(hidden_binary)

    # Additional sanity check: if result is empty or looks like garbage, raise error
    if not hidden_text.strip():
        raise ValueError("No hidden message found.")

    # Optional: Check if contains mostly printable characters, else raise error
    if not all(32 <= ord(c) <= 126 or c in '\n\r\t' for c in hidden_text):
        raise ValueError("No hidden message found.")

    return hidden_text
