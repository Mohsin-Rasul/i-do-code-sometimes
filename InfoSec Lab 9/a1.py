import random

def power(a, b, p):
    res = 1
    a = a % p
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % p
        a = (a * a) % p
        b = b // 2
    return res

def modInverse(a, p):
    a = a % p
    for x in range(1, p):
        if (a * x) % p == 1:
            return x
    return None

def keyGeneration():
    P = 467
    E1 = 2
    D = random.randint(2, P - 2)
    E2 = power(E1, D, P)
    publicKey = (E1, E2, P)
    privateKey = D
    print(f"Public Key (E1, E2, P): {publicKey}")
    print(f"Private Key D: {privateKey}")
    return publicKey, privateKey

def encrypt(plainText, publicKey):
    E1, E2, P = publicKey
    R = random.randint(2, P - 2)
    C1 = power(E1, R, P)
    C2 = (plainText * power(E2, R, P)) % P
    print(f"Random R: {R}")
    print(f"Cipher Text (C1, C2): ({C1}, {C2})")
    return C1, C2

def decrypt(C1, C2, privateKey, P):
    D = privateKey
    C1D = power(C1, D, P)
    C1DInv = modInverse(C1D, P)
    plainText = (C2 * C1DInv) % P
    return plainText

def main():
    publicKey, privateKey = keyGeneration()
    PT = int(input("Enter Plain Text (integer): "))
    C1, C2 = encrypt(PT, publicKey)
    recoveredPT = decrypt(C1, C2, privateKey, publicKey[2])
    print(f"Recovered Plain Text: {recoveredPT}")

if __name__ == "__main__":
    main()