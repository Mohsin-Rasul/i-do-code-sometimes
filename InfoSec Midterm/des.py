from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key=b'abcdefgh'  # DES key must be 8 bytes
ogtext=b"mohsin"
paddedtext=pad(orignal,DEC.block_size)
des = DES.new(key,DES.MODE_ECB)

ciphertext=des.encrypt(paddedtext)
plaintext= des.decrypt(ciphertext)
plaintext=unpad(plaintext,DES.block_size)


