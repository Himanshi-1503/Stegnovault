# Stegnovault
Project Description: Image Steganography
Overview
This Image Steganography project is designed to hide and retrieve encrypted messages within image files. It provides a secure way to encode and decode messages using a graphical user interface built with tkinter. The project leverages the cryptography library's Fernet class for encryption and decryption, ensuring that the hidden messages are protected with a user-provided password.

Key Features
Graphical User Interface (GUI):

The application features a user-friendly GUI built with tkinter, allowing users to easily navigate through the encoding and decoding processes.
Users can select images, enter messages, and provide passwords through intuitive dialog boxes.
Encryption and Decryption:

Messages are encrypted using the cryptography library's Fernet class, which provides symmetric encryption.
The user-provided password is used to generate a key for encryption and decryption, ensuring that only users with the correct password can access the hidden message.
Encoding and Decoding:

The application encodes the encrypted message into the image's pixel data, maintaining the visual integrity of the image.
During decoding, the application retrieves the hidden data from the image and decrypts it using the provided password.
Additional Functionalities:

The application includes features for image preview, displaying hidden messages, and reading the hidden text aloud using the pyttsx3 library.
An information dialog provides details about the original and decoded images, such as their sizes and dimensions.
How It Works
Encoding Process:

The user selects an image and enters the message they want to hide.
The user provides a password, which is used to encrypt the message.
The encrypted message is encoded into the image's pixel data.
The modified image is saved, containing the hidden message.
Decoding Process:

The user selects an image with a hidden message.
The user provides the password used during the encoding process.
The application retrieves the hidden data from the image and decrypts it using the provided password.
The decrypted message is displayed to the user.
Code Structure
Main Class (Stegno): Contains methods for encoding and decoding messages, handling GUI interactions, and managing encryption and decryption.
GUI Methods: Methods like frame1_encode, frame2_encode, frame1_decode, and frame2_decode handle the user interface for encoding and decoding processes.
Encryption and Decryption: Methods like enc_fun, encode_enc, decode, and modPix manage the encryption, encoding, decoding, and pixel manipulation processes.
Utility Methods: Methods like genData, read_aloud, page3, and info provide additional functionalities such as data conversion, text-to-speech, navigation, and information display.
Libraries Used
tkinter: For building the graphical user interface.
PIL (Pillow): For image processing and manipulation.
cryptography: For encrypting and decrypting messages.
pyttsx3: For text-to-speech functionality.
This project demonstrates the practical application of steganography and encryption techniques, providing a secure and user-friendly way to hide and retrieve messages within images.
