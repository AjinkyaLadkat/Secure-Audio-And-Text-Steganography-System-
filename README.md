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

## 🔐 Security Overview

This project is designed with multi-layered security to ensure **confidential and safe communication** via multimedia files:

### 1. **Message Encryption Before Embedding**  
- The secret message you enter is **encrypted using AES-256 symmetric encryption** before being hidden inside images or audio. This means the hidden data is **ciphertext**, not plain text. Even if an attacker extracts the embedded bits, they only get encrypted gibberish.

### 2. **Password-Based Key Derivation (KDF)**  
- Your password is not used directly. Instead, it is **stretched and salted** using a strong Key Derivation Function such as PBKDF2 (that internally uses SHA-256) to produce a unique, strong encryption key every time. This protects against brute-force and rainbow table attacks.

### 3. **Temporary Key Usage**  
- The encryption key derived from your password is **only used in memory during runtime** and is **never saved** or stored in the file or anywhere else. This prevents key leakage.

### 4. **Least Significant Bit (LSB) Steganography**  
- The encrypted message bits are embedded in the **least significant bits** of image pixels or audio samples. LSB steganography is subtle and difficult to detect, making the hidden message invisible to casual inspection.

### 5. **Salt Enhances Security**  
- By adding a **random salt** to the password during key derivation, even the same password will generate different keys every time, **increasing resistance against attacks** and ensuring unique encryption.

### 6. **Combined Defense-in-Depth Approach**  
- This project **combines cryptography and steganography**, which means:
    - **Cryptography** ensures that the message content is unreadable without the password.
    - **Steganography** hides the very existence of the message.

Together, these layers make unauthorized detection and decryption **exceedingly difficult**.

---

### How You Can Maximize Security

- Use **strong, unique passwords** — longer passphrases with a mix of characters.
- Protect your password from exposure.
- Avoid uploading or sharing your original media files publicly after embedding sensitive data.

---

## Project Structure

    ├── app.py                              # Main Streamlit app
    ├── stegano_utils.py                    # Image steganography functions
    ├── audio_stegano_utils.py              # Audio steganography functions
    ├── crypto_utils.py                     # Encryption/decryption helpers
    ├── audio_converter.py                  # Converts MP3 to WAV for processing
    ├── assets/                             # Sample media files (excluded from Git)
    ├── test_files/                         # Test files used for development & validation
        ├── test_audi_workflow.py
        ├── test_crypto.py
        ├── test_stegano.py
    ├── requirements.txt                    # Python dependencies
    └── README.md                           # Project documentation


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

## Future Scope 🚀

This multimedia steganography system provides a powerful foundation for a wide range of advanced and impactful applications:

- **Video Steganography Integration:** Extend the system to support embedding encrypted messages within video files by manipulating both visual frames and audio tracks, enabling richer data hiding with higher capacity and stealth.

- **Military and Confidential Communications:** Adapt this technology for secure, covert communication in defense sectors, enabling confidential message exchange over public or compromised channels without raising suspicion.

- **Advanced Cryptographic Protocols:** Integrate hybrid encryption methods combining symmetric and asymmetric cryptography (e.g., AES + RSA) for enhanced security and scalable key management in multi-user environments.

- **IoT and Edge Device Security:** Embed hidden encrypted commands or data within multimedia files transmitted across IoT networks to safeguard against interception and tampering in resource-constrained devices.

- **Steganographic Watermarking for Digital Rights Management (DRM):** Embed imperceptible encrypted watermarks into media files to verify ownership, prevent piracy, and track content distribution.

- **Resilient Steganography with Error Detection & Correction:** Implement robust algorithms to detect and recover from data corruption or intentional tampering, ensuring message integrity in hostile environments.

- **Integration with Blockchain for Secure Provenance:** Combine steganography with blockchain to immutably record and verify the origin and integrity of hidden messages or digital assets.

- **Secure Cloud Storage Solutions:** Use encrypted steganography to store sensitive data covertly within innocuous media files in cloud storage, protecting data privacy even if the storage provider is compromised.

- **AI-Enhanced Steganalysis Resistance:** Employ machine learning to dynamically adapt embedding techniques to evade increasingly sophisticated steganalysis and forensic detection methods.

- **Cross-Platform Mobile and Web Applications:** Expand to mobile and progressive web apps, enabling users to securely hide and extract confidential messages on any device anytime, anywhere.

- **Real-Time Encrypted Multimedia Messaging:** Develop real-time chat and multimedia sharing platforms where messages are encrypted and hidden within media files, combining privacy and stealth.

This project unlocks numerous pathways toward pioneering secure communication technologies with real-world significance in defense, privacy, digital rights, and beyond. The fusion of multimedia steganography and encryption presents exciting opportunities to innovate at the cutting edge of cybersecurity and data protection.


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
