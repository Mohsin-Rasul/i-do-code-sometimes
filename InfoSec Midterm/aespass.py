import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def getK(uPass):
    return hashlib.sha256(uPass.encode()).digest()

def encFile(fPath, uPass):
    k = getK(uPass)
    iv = os.urandom(16)
    fSize = os.path.getsize(fPath)
    
    aesObj = AES.new(k, AES.MODE_CBC, iv)
    encPath = "(enc)" + fPath
    
    with open(fPath, 'rb') as fIn, open(encPath, 'wb') as fOut:
        fOut.write(fSize.to_bytes(8, 'big'))
        fOut.write(iv)
        while True:
            chunk = fIn.read(65536)
            if len(chunk) == 0:
                break
            if len(chunk) % 16 != 0:
                chunk = pad(chunk, 16)
            fOut.write(aesObj.encrypt(chunk))
    return encPath

def decFile(encPath, uPass):
    k = getK(uPass)
    with open(encPath, 'rb') as fIn:
        fSize = int.from_bytes(fIn.read(8), 'big')
        iv = fIn.read(16)
        aesObj = AES.new(k, AES.MODE_CBC, iv)
        
        decPath = encPath.replace("(enc)", "(dec)")
        with open(decPath, 'wb') as fOut:
            while True:
                chunk = fIn.read(65536)
                if len(chunk) == 0:
                    break
                dChunk = aesObj.decrypt(chunk)
                fOut.write(dChunk)
            fOut.truncate(fSize)
    return decPath

p = input("Enter password: ")
f = "message.txt"
with open(f, "w") as m: m.write("This is a test message for AES-CBC file encryption.")

eFile = encFile(f, p)
print(f"File encrypted: {eFile}")

dFile = decFile(eFile, p)
print(f"File decrypted: {dFile}")
