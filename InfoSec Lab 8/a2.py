def checkIsPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def checkIsSemiprime(n):
    for i in range(2, n):
        if checkIsPrime(i) and n % i == 0:
            j = n // i
            if checkIsPrime(j):
                return True
    return False

eNum = list(range(29, 51))
plist = []

for aNum in eNum:
    if checkIsPrime(aNum) or checkIsSemiprime(aNum):
        plist.append(aNum)

print("Prime or Semiprime numbers between 29 and 50:")
print(plist)