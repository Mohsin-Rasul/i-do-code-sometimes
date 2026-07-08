numTerms = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

if numTerms <= 0:
    print("Please enter a positive integer.")
elif numTerms == 1:
    print(f"Fibonacci series up to {numTerms}: {a}")
else:
    print("Fibonacci series:", end=" ")
    while count < numTerms:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1