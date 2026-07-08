p = 61
q = 53

n = p * q

phi = (p - 1) * (q - 1)

e = 17 

def modInverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

d = modInverse(e, phi)

def encrypt(message):
    cipher = pow(message, e, n)
    return cipher

def decrypt(cipher):
    message = pow(cipher, d, n)
    return message

message = 65 

cipherText = encrypt(message)
decryptedText = decrypt(cipherText)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
print("Original Message:", message)
print("Encrypted Message:", cipherText)
print("Decrypted Message:", decryptedText)