def ceasar(plaintext,shift):
    alpha="abcdefghijklmnopqrstuvwxyz"
    result=""
    for i in plaintext.lower():
        if i.isalpha():
            result+=alpha[(alpha.index(i)+shift)%26]
        else:
            result+=i
    return result

text="Mohsin"
cipher=ceasar(text,3)
print(cipher)