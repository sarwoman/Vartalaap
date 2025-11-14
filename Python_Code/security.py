"""
# Hash a Password using bcrypt

import bcrypt

password = "Sarwajeet"

encoded_password = password.encode("utf-8")

print(encoded_password)

salt = bcrypt.gensalt()

print(salt)

hashed_password = bcrypt.hashpw(encoded_password , salt)

print("Hashed Password : ",hashed_password)

# Verify the Password Typed

user_password = input("Enter Password : ").encode()

if bcrypt.checkpw(user_password , hashed_password):
    print("Password matches")

else:
    print("Password does not match")

"""

"""
# Validate the Password Typed

import re

password = "Sarwajeet123@"

reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,15}$"

# Compile regex

pattern = re.compile(reg)

print(pattern)

# Search Pattern in Password

match = re.search(pattern,password)

if match:
    print("Password is valid")

else:
    print("Password Invalid")

"""

#Implement Encryption using Asymmetric Encryption

import rsa

publicKey , privateKey = rsa.newkeys(512)

message = "Hey,how are u ?"

encrypted_message = rsa.encrypt(message.encode() , publicKey)

print("Orinal Message : ",message)
print("Encrypted Message : ",encrypted_message)

decrypted_message = rsa.decrypt(encrypted_message , privateKey).decode()

print("Decrypted Message : ",decrypted_message)


# Encryption using symmetric Encryption

from cryptography.fernet import Fernet

key = Fernet.generate_key()

print("Key : ",key)

f = Fernet(key)

message = "Hey , Hello"

encrypted_message = f.encrypt(message.encode())

print("Encrypted Message : ",encrypted_message)

decrypted_message = f.decrypt(encrypted_message)

print("Decrypted Message : ",decrypted_message.decode())

