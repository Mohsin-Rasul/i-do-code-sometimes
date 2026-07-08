def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def totient(n):
    cnt = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            cnt += 1
    return cnt

for n in range(1, 21):
    print(f"phi({n}) = {totient(n)}")