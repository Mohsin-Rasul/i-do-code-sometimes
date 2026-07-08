import hashlib

def md5Hash(message):
    return hashlib.md5(message.encode()).hexdigest()

msg = input("Enter message for MD5: ")
print("MD5 Hash:", md5Hash(msg))