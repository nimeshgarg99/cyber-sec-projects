from cryptography.fernet import Fernet
import os
def generate_key():
    key = Fernet.generate_key()
    with open ("Secret.key", "wb") as key_file: 
        key_file.write(key)
    
def load_key():
    return open("secret.key", "rb").read()

def encrypt (filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except :
            return
    with open(filename, "wb") as file:
        file.write(decrypted_data)
choice = input("enter 'e' to encrypt or 'd' decrypt the file").lower()
if choice == 'e':
    filename = input("enter file name: ")
    if os.path.exists(filename):
        generate_key()
        key = load_key()
        encrypt(filename, key)
        print("file is successfully encrypted")

    else:
        print("check filename again")

elif choice == 'd':
    filename = input("enter file name: ")
    if os.path.exists(filename):
        
        key = load_key()
        decrypt(filename, key)
        print("file is successfully decrypted")

    else:
        print("check filename again")
