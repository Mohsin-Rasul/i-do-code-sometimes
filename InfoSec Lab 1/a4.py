studentMarks = int(input("Enter student marks (1-100): "))

if studentMarks < 1 or studentMarks > 100:
    print("Invalid input. Please enter marks between 1 and 100.")
elif studentMarks < 50:
    print("Grade: F")
elif studentMarks <= 60:
    print("Grade: E")
elif studentMarks <= 70:
    print("Grade: D")
elif studentMarks <= 80:
    print("Grade: C")
elif studentMarks <= 90:
    print("Grade: B")
else:
    print("Grade: A")