def gcd(a, b):
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return a

n1 = 18
n2 = 12

res = gcd(n1, n2)
print(f"GCD of {n1} and {n2} is {res}")