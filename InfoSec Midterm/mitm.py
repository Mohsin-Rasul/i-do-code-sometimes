!pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
from collections import defaultdict

def make_des_key_from_int(k_int):
    return k_int.to_bytes(8,byteorder="big")

def des_encrypt_block(key,block):
    cipher = DES.new(key,DES.MODE_ECB)
    return cipher.encrypt(block)

def des_decrypt_block(key,block):
    cipher = DES.new(key,DES.MODE_ECB)
    return cipher.decrypt(block)

def des_encrypt_msg(key,msg):
    cipher = DES.new(key,DES.MODE_ECB)
    return cipher.encrypt(pad(msg,8))

def des_decrypt_msg(key,msg):
    cipher= DES.new(key,DES.MODE_ECB)
    return unpad(cipher.decrypt(msg),8)

def format_key(k,bits):
    return format(k,f"0{bits}b")


def mitm_attack(p_block,c_block,bits):
    table=defaultdict(list)
    KEYSPACE=1<<bits

    for k1 in range(KEYSPACE):
        key=make_des_key_from_int(k1)
        mid=des_decrypt_block(key,c_block)
        table[mid].append(k1)


    candidates=[]
    for k2 in range(KEYSPACE):
        key=make_des_key_from_int(k2)
        mid=des_decrypt_block(key,c_block)
        if mid in table:
            for k1 in table[mid]:
                candidates.append((k1,k2))
    return candidates

bits =12
k1_real=45
k2_real=99

plaintext="helle"
padded=pad(plaintext,8)
p_block=padded[:8]
cipher=encrypt
