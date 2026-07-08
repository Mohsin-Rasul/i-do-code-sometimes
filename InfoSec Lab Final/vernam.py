def vernamChipher(text,key):
    result=""
    for i in range(len(text)):
        result+=chr(ord(text[i])^ord(key[i % len(key)]))
    return result

plaintext="Mohsin"
key="Attack"
cipher=vernamChipher(plaintext,key)
print(cipher)