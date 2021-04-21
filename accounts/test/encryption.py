# from base64 import b64encode, b64decode
# import hashlib
# from Cryptodome.Cipher import AES
# import os
# from Cryptodome.Random import get_random_bytes

# def encrypt(plain_text, password):
#     # generate a random salt
#     salt = get_random_bytes(AES.block_size)

#     # use the Scrypt KDF to get a private key from the password
#     private_key = hashlib.scrypt(
#         password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

#     # create cipher config
#     cipher_config = AES.new(private_key, AES.MODE_GCM)

#     # return a dictionary with the encrypted text
#     cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
#     return {
#         'cipher_text': b64encode(cipher_text).decode('utf-8'),
#         'salt': b64encode(salt).decode('utf-8'),
#         'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
#         'tag': b64encode(tag).decode('utf-8')
#     }


# def decrypt(enc_dict, password):
#     # decode the dictionary entries from base64
#     salt = b64decode(enc_dict['salt'])
#     cipher_text = b64decode(enc_dict['cipher_text'])
#     nonce = b64decode(enc_dict['nonce'])
#     tag = b64decode(enc_dict['tag'])
    

#     # generate the private key from the password and salt
#     private_key = hashlib.scrypt(
#         password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

#     # create the cipher config
#     cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

#     # decrypt the cipher text
#     decrypted = cipher.decrypt_and_verify(cipher_text, tag)

#     return decrypted


# def main():
#     password = input("Password: ")

#     # First let us encrypt secret message
#     encrypted = encrypt("hello", password)
#     print(encrypted)

#     # Let us decrypt using our original password
#     decrypted = decrypt(encrypted, password)
#     print(bytes.decode(decrypted))

# main()

# AES 256 encryption/decryption using pycrypto library
 
# import base64
# import hashlib
# from Crypto.Cipher import AES
# from Crypto import Random
 
# BLOCK_SIZE = 16
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
# unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
# password = input("Enter encryption password: ")
 
 
# def encrypt(raw, password):
#     private_key = hashlib.sha256(password.encode("utf-8")).digest()
#     raw = pad(raw)
#     iv = Random.new().read(AES.block_size)
#     cipher = AES.new(private_key, AES.MODE_CBC, iv)
#     return base64.b64encode(iv + cipher.encrypt(raw))
 
 
# def decrypt(enc, password):
#     private_key = hashlib.sha256(password.encode("utf-8")).digest()
#     enc = base64.b64decode(enc)
#     iv = enc[:16]
#     cipher = AES.new(private_key, AES.MODE_CBC, iv)
#     return unpad(cipher.decrypt(enc[16:]))
 
 
# # First let us encrypt secret message
# encrypted = encrypt("This is a secret message", password)
# print(encrypted)
 
# # Let us decrypt using our original password
# decrypted = decrypt(encrypted, password)
# print(bytes.decode(decrypted))


# AES 256 encryption/decryption using pycrypto library
 
import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
password = input("Enter encryption password: ")
 
 
def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key
 
 
def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc, password):
    private_key = get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
 
 
# First let us encrypt secret message
encrypted = encrypt("This is a secret message", password)
print(encrypted)
 
# Let us decrypt using our original password
decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))