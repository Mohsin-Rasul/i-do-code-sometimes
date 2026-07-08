p=61
q=53
n=p*q
phi=(p-1)*(q-1)
e=17

for i in range(1,phi):
    if (e*i) % phi ==1:
        d=i
        break
msg=65

cipher=pow(msg,e,n)
decryt=pow(cipher,d,n)

print(cipher)
print(decryt)
