from Crypto.Cipher import AES
import base64


# class Encryption():
#     # plainText = 'FirstSoft Technologies Pvt Ltd'

#     # secret_key = '123'.rjust(16).encode()

def encryptit(plainText):
    bytecode = plainText.rjust(32).encode()
    secret_key = '123'.rjust(16).encode()
    cipher = AES.new(secret_key, AES.MODE_ECB)
    encryptedText = base64.b64encode(cipher.encrypt(bytecode)).decode()
    
    return encryptedText

def decryptit(encryptedText):

    secret_key = '123'.rjust(16).encode()
    cipher = AES.new(secret_key, AES.MODE_ECB)
    plainText = cipher.decrypt(base64.b64decode(encryptedText))
    return plainText.decode()

