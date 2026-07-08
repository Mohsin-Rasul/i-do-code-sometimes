import hashlib

def hashPassword(password):
    return hashlib.md5(password.encode()).hexdigest()

userPassword = input("Enter your password: ")
hashedOutput = hashPassword(userPassword)

print("Hashed Password (MD5):", hashedOutput)