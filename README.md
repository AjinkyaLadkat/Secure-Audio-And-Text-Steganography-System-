# 🔐 Multimedia Steganography System - Image & Audio with Encryption

A secure and user-friendly steganography tool built with Streamlit that allows you to embed secret messages inside images and audio files. This project combines multimedia steganography techniques with AES encryption to ensure your hidden messages remain safe and private.

---

## Features

- **Image Steganography:** Hide encrypted text messages inside PNG, JPG, and JPEG images using LSB (Least Significant Bit) technique.
- **Audio Steganography:** Embed encrypted messages within WAV and MP3 audio files by modifying the least significant bits of audio frames.
- **AES Encryption:** Messages are encrypted with a user-defined password before embedding, providing an extra layer of security.
- **Easy to Use:** Intuitive web interface powered by Streamlit, enabling quick upload, embedding, extraction, and download of files.
- **Supports multiple media types:** Seamlessly switch between image and audio modes for both embedding and extraction.

---

## Project Structure

    ├── app.py # Main Streamlit app
    ├── stegano_utils.py # Image steganography functions
    ├── audio_stegano_utils.py # Audio steganography functions
    ├── crypto_utils.py # Encryption/decryption helpers
    ├── audio_converter.py # Converts MP3 to WAV for processing
    ├── assets/ # Sample media files (excluded from Git)
    ├── test_files/ # Test files used for development & validation
    ├── requirements.txt # Python dependencies
    └── README.md # Project documentation


### About `test_files/` folder

The `test_files/` folder contains a set of example images and audio clips specifically chosen to test the embedding and extraction processes during development. These files help ensure:

- The robustness of the steganography algorithms across different media types and formats.
- The encryption and decryption workflows are working correctly.
- Consistent and reliable UI experience while testing edge cases and typical usage scenarios.

---

## Installation & Running Locally

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

## Live Demo

Check out the live app hosted on Hugging Face Spaces:  
[https://huggingface.co/spaces/AjinkyaLadkat/Secure-Multimedia-Steganography-System-With-AES-Encryption](https://huggingface.co/spaces/AjinkyaLadkat/Secure-Multimedia-Steganography-System-With-AES-Encryption)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Inspired by the need for secure communication using multimedia files.  
- Thanks to the open-source community for the amazing libraries used here.

---

If you find this project useful or have suggestions, feel free to open an issue or a pull request. Happy hiding! 🔐
