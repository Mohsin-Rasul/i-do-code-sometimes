userNums = input("Enter a set of integers separated by spaces: ").split()
evenSum = 0
oddSum = 0

for n in userNums:
    if n.lstrip('-').isdigit():
        val = int(n)
        if val % 2 == 0:
            evenSum += val
        else:
            oddSum += val

print(f"Sum of Even Integers: {evenSum}")
print(f"Sum of Odd Integers: {oddSum}")