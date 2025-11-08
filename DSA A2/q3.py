class TwoStacks:
    # Implements two stacks in one list.
    
    def __init__(self, n):
        """
        Initializes the list of size n, and the two top pointers.
        Stack 1 grows from left, Stack 2 grows from right.
        """
        self.size = n
        self.arr = [None] * n
        self.top1 = -1           # Top for stack 1 (starts at -1)
        self.top2 = self.size    # Top for stack 2 (starts at size)

    def push1(self, value):
        """
        Pushes a value onto stack 1.
        """
        # Check if there is space between the two tops
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            # No space, raise overflow exception
            raise Exception("Stack Overflow: List is full")

    def push2(self, value):
        """
        Pushes a value onto stack 2.
        """
        # Check if there is space
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            # No space, raise overflow exception
            raise Exception("Stack Overflow: List is full")

    def pop1(self):
        """
        Pops a value from stack 1.
        """
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.arr[self.top1] = None # Optional: clear the data
            self.top1 -= 1
            return value
        else:
            raise Exception("Stack 1 is empty (Underflow)")

    def pop2(self):
        """
        Pops a value from stack 2.
        """
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.arr[self.top2] = None # Optional: clear the data
            self.top2 += 1
            return value
        else:
            raise Exception("Stack 2 is empty (Underflow)")

    def display(self):
        """
        Helper function to show the current state of the list.
        """
        print(f"List: {self.arr}")
        print(f"Top1: {self.top1}, Top2: {self.top2}")


# --- Main Program Execution ---
try:
    stacks = TwoStacks(5) # Create two stacks in a list of size 5

    stacks.push1(10)
    stacks.push1(20)
    stacks.push2(50)
    stacks.push2(40)
    
    print("--- After pushing 4 items ---")
    stacks.display()
    
    stacks.push1(30) # This should fill the list
    
    print("\n--- After filling the list ---")
    stacks.display()
    
    print(f"\nPopped from stack 1: {stacks.pop1()}")
    print(f"Popped from stack 2: {stacks.pop2()}")

    print("\n--- After popping ---")
    stacks.display()
    
    print("\n--- Trying to cause overflow ---")
    stacks.push1(33)
    stacks.push2(44) # This one should fail
    stacks.push2(99) # This will not be reached

except Exception as e:
    print(f"An error occurred: {e}")
