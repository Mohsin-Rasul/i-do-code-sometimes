numVal = int(input("Enter a number to calculate its factorial: "))
factResult = 1

if numVal < 0:
    print("Factorial is not defined for negative numbers.")
elif numVal == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, numVal + 1):
        factResult *= i
    print(f"The factorial of {numVal} is {factResult}")