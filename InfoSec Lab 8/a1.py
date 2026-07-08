def calculateGcd(a, b):
    if b == 0:
        return a
    else:
        return calculateGcd(b, a % b)

print("The GCD of 67 and 128 is:", calculateGcd(67, 128))