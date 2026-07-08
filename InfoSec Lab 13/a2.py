import hashlib

with open("message.txt", "r") as file:
    data = file.read()

hash1 = hashlib.md5(data.encode()).hexdigest()

print("Original File MD5 Hash:", hash1)