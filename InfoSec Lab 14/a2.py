import hashlib

with open("message.txt", "r") as file:
    data = file.read()

hash1 = hashlib.sha256(data.encode()).hexdigest()

print("Original File Hash:", hash1)