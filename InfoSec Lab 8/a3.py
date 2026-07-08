def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fermatCheck(a, p):
    if a % p == 0:
        return False
    return (a**(p-1)) % p == 1

pVal = 17
aVal = 2

if isPrime(pVal):
    print(f"{pVal} is prime")
    if fermatCheck(aVal, pVal):
        print(f"Fermat's theorem holds: {aVal}^({pVal}-1) % {pVal} == 1")
    else:
        print(f"Fermat's theorem does NOT hold for a={aVal} and p={pVal}")
else:
    print(f"{pVal} is not prime")