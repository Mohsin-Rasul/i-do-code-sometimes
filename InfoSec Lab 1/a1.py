userInput = input("Enter an integer: ")

if userInput.isdigit() or (userInput.startswith('-') and userInput[1:].isdigit()):
    reversedNum = userInput[::-1]
    
    if reversedNum.endswith('-'):
        reversedNum = '-' + reversedNum[:-1]
        
    print(f"Reversed Output: {reversedNum}")
else:
    print("Invalid input. Please enter an integer.")