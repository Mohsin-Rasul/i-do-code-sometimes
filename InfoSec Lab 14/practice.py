import hashlib

def hashPassword(password):
    return hashlib.sha512(password.encode()).hexdigest()

userPassword = input("Enter your password: ")
hashedOutput = hashPassword(userPassword)

print("Hashed Password (SHA-512):", hashedOutput)