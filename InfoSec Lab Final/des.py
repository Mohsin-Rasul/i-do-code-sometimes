from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad

key=b"8charkey"
data=b"Mohsin"

cipher=DES.new(key,DES.MODE_ECB)
ciphertext=cipher.encrypt(pad(data,DES.block_size))

decipher=DES.new(key,DES.MODE_ECB)
decrypt=unpad(decipher.decrypt(ciphertext),DES.block_size)

print(decrypt.decode())