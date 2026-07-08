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

message = input("Enter a message to sign: ")
messageNum = sum([ord(c) for c in message]) 

def signMessage(messageNum, d, n):
    signature = pow(messageNum, d, n)
    return signature

def verifySignature(signature, e, n):
    verifiedMessage = pow(signature, e, n)
    return verifiedMessage

signature = signMessage(messageNum, d, n)
verifiedMessage = verifySignature(signature, e, n)

print("\nOriginal Message (numeric):", messageNum)
print("Digital Signature:", signature)
print("Verified Message:", verifiedMessage)
print("Message Verified:", verifiedMessage == messageNum)