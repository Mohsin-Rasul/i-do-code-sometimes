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

def signMessage(messageNum, d, n):
    signature = pow(messageNum, d, n)
    return signature

def verifySignature(signature, e, n):
    verifiedMessage = pow(signature, e, n)
    return verifiedMessage

studentName = input("Enter student name: ")
message = input("Enter a message to sign: ")

messageNum = sum([ord(c) for c in message]) 

signature = signMessage(messageNum, d, n)
verifiedMessage = verifySignature(signature, e, n)

print(f"\n--- Digital Signature Report for {studentName} ---")
print("Original Message (numeric):", messageNum)
print("Digital Signature Block:", signature)
print("Verified Message Result:", verifiedMessage)
print("Integrity & Authentication Verified:", verifiedMessage == messageNum)