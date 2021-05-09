from cryptography.fernet import Fernet

# using the generated key


def encFile(filepath):
    fernet = Fernet(b'm-RfRzx3i-0qMm1EzuNOoh10U7RXpun5VdXTIng8LP8=')
    with open(filepath, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(encrypted)


def decFile(filepath):
    fernet = Fernet(b'm-RfRzx3i-0qMm1EzuNOoh10U7RXpun5VdXTIng8LP8=')
    with open(filepath, 'rb') as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filepath, 'wb') as dec_file:
        dec_file.write(decrypted)
    print(decrypted)

# m-RfRzx3i-0qMm1EzuNOoh10U7RXpun5VdXTIng8LP8=