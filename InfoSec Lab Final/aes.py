from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key=get_random_bytes(32)
data=b"Mohsin BCY243024"

cipher=AES.new(key,AES.MODE_GCM)
ciphertext,tag=cipher.encrypt_and_digest(data)

decipher=AES.new(key,AES.MODE_GCM,nonce=cipher.nonce)
decrypt=decipher.decrypt_and_verify(ciphertext,tag)

print("Decrypt",decrypt.decode())
