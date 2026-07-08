key="abcdefghijklmnopqrstuvwxyz"

def encSubstitution(n,plaintext):
    result=""
    for l in plaintext.lower():
        try:
            i=(key.index(l)+n)%26
            result+=key[i]
        except ValueError:
            result+=l
    return result
def decSubstitution(n,ciphertext):
    result=""
    for l in ciphertext.lower():
        try:
           i=(key.index(l)-n)%26
           result+=key[i]
        except ValueError:
            result+=l
    return result

plaintext="kuchbhi"
c=encSubstitution(13,plaintext)
d=decSubstitution(13,c)
print("plain",plaintext)
print("cipher",c)
print("dec",d)