def shiftEnc(c,n):
    if c.isalpha():
        c= c.upper()
        return chr(((ord(c)-ord("A")+n)% 26)+ ord("A"))
    else:
        return c
    
def shiftDec(c,n):
    if c.isalpha():
        c=c.upper()
        return chr(((ord(c)-ord("A")-n)%26)+ord("A"))
    else:
        return c
    
def keyVigenere(key):
    keyArray=[]
    for i in range(len(key)):
        keyElement=ord(key[i].upper()) - 65
        keyArray.append(keyElement)
    return keyArray

def encVigenere(plaintext,key):
    secret="".join([
        shiftEnc(plaintext[i],key[i%len(key)]) if plaintext[i].isalpha() else plaintext[i]
        for i in range(len(plaintext))
    ])
    return secret

def decVigenere(ciphertext,key):
    secret="".join([
        shiftDec(ciphertext[i],key[i%len(key)]) if ciphertext[i].isalpha() else ciphertext[i]
        for i in range(len(ciphertext))
    ])
    return secret

sKey="DECLARATION"
key=keyVigenere(sKey)

p="Mohsin"
ciphertext=encVigenere(p,key)
print("Enc",ciphertext)

dec=decVigenere(ciphertext,key)
print("dec",dec)