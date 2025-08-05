import streamlit as st
import os
import tempfile
from stegano_utils import hide_text_in_image, reveal_text_from_image
from audio_stegano_utils import embed_text_in_audio, extract_text_from_audio
from audio_converter import mp3_to_wav
from crypto_utils import encrypt_message, decrypt_message



# Ensure temp directory exists
if not os.path.exists("temp"):
    os.makedirs("temp")

# Title
st.markdown("<h1 style='margin-bottom: 0;'>🔐 Multimedia Steganography System</h1>", unsafe_allow_html=True)

# Subtitle — smaller than title, bigger than normal text
st.markdown("<h3 style='color: #DBAC53; margin-top: 4px;'>Steganography Meets Encryption — Safe, Simple, Smart</h3>", unsafe_allow_html=True)


st.markdown("""
> **Multimedia steganography** is the art of hiding secret information inside digital media such as images and audio files. 
> Unlike encryption alone, it conceals the very existence of the hidden message, offering a stealthy and secure method of communication.
""")


tab1, tab2 = st.tabs(["📝 Embed Secret Message", "🔓 Extract Secret Message"])

# ----------------- EMBED TAB -----------------
with tab1:
    file_type = st.radio("Select File Type", ["Image", "Audio"], key="embed_type")
    uploaded_file = st.file_uploader(f"Upload {file_type} file to embed message")
    secret_message = st.text_area("Enter the secret message to embed")
    password = st.text_input("🔑 SET PASSWORD", type="password")

    if st.button("Submit"):
        if not uploaded_file:
            st.warning("⚠️ Please upload a file.")
        elif not secret_message.strip():
            st.warning("⚠️ Please enter a secret message.")
        elif not password:
            st.warning("⚠️ Please set a password.")
        else:
            filename = uploaded_file.name.lower()
            is_image = filename.endswith((".png", ".jpg", ".jpeg"))
            is_audio = filename.endswith((".mp3", ".wav"))

            if file_type == "Image" and not is_image:
                st.error("❌ Uploaded file is not an image.")
            elif file_type == "Audio" and not is_audio:
                st.error("❌ Uploaded file is not an audio file.")
            else:
                try:
                    # Encrypt the message first
                    encrypted_message = encrypt_message(secret_message, password)

                    if file_type == "Image":
                        image_path = os.path.join("temp", uploaded_file.name)
                        with open(image_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())

                        output_path = hide_text_in_image(image_path, encrypted_message)
                        st.success("✅ Encrypted message embedded in image!")
                        st.image(output_path)
                        st.download_button("Download Image with Hidden Message", data=open(output_path, "rb"), file_name="hidden_image.png")

                    else:
                        mp3_path = os.path.join("temp", uploaded_file.name)
                        with open(mp3_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())

                        with tempfile.TemporaryDirectory() as tempdir:
                            wav_path = os.path.join(tempdir, "original.wav")
                            stego_wav_path = os.path.join(tempdir, "stego.wav")

                            mp3_to_wav(mp3_path, wav_path)
                            embed_text_in_audio(wav_path, stego_wav_path, encrypted_message)

                            st.success("✅ Encrypted message embedded in audio!")
                            st.audio(stego_wav_path)
                            with open(stego_wav_path, "rb") as f:
                                st.download_button("Download Audio with Hidden Message", data=f, file_name="hidden_audio.wav")
                except Exception as e:
                    st.error(f"Encryption or embedding failed: {str(e)}")

with tab2:
    file_type = st.radio("Select File Type", ["Image", "Audio"], key="extract_type")
    uploaded_file = st.file_uploader(f"Upload {file_type} file to extract message", key="extract_file")

    if uploaded_file:
        filename = uploaded_file.name.lower()
        is_image = filename.endswith((".png", ".jpg", ".jpeg"))
        is_audio = filename.endswith((".mp3", ".wav"))

        if file_type == "Image" and not is_image:
            st.error("❌ Uploaded file is not an image.")
        elif file_type == "Audio" and not is_audio:
            st.error("❌ Uploaded file is not an audio file.")
        else:
            try:
                encrypted_message = None

                if file_type == "Image":
                    image_path = os.path.join("temp", uploaded_file.name)
                    with open(image_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    encrypted_message = reveal_text_from_image(image_path)

                else:
                    audio_path = os.path.join("temp", uploaded_file.name)
                    with open(audio_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    encrypted_message = extract_text_from_audio(audio_path)

                if not encrypted_message or encrypted_message.strip() == "":
                    st.warning("⚠️ No hidden message found.")
                else:
                    # Hidden message exists, now show password input and Extract button
                    password = st.text_input("🔑 ENTER PASSWORD", type="password", key="pwd_input")

                    if st.button("Extract"):
                        if not password:
                            st.warning("⚠️ Please enter the password.")
                        else:
                            try:
                                decrypted_message = decrypt_message(encrypted_message, password)
                                st.success("✅ Message extracted successfully:")
                                st.write(decrypted_message)
                            except Exception:
                                st.error("❌ Decryption failed. Incorrect password or corrupted data.")

                    else:
                        st.info("🔐 Hidden message detected. Please enter password and click Extract.")
            except Exception as e:
                st.error(f"Extraction failed: {str(e)}")
