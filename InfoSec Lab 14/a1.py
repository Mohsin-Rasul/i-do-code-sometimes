import hashlib

def sha512Hash(message):
    return hashlib.sha512(message.encode()).hexdigest()

msg = input("Enter message for SHA-512: ")
print("SHA-512 Hash:", sha512Hash(msg))