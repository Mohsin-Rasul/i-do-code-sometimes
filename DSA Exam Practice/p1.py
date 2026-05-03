class Stack:
    def __init__(self):
        self.stack=[]

    def push (self,course):
        self.stack.append(course)
        print("Added course:",course)
        print("Current stacl:",self.stack)


    def pop(self):
        if not self.stack:
            print("Stack is empty:")
        else:
            rem=self.stack.pop()
            print("Removed Course:",rem)

    def peek(self):
        if not self.stack:
            print("stack is emmpty")
        else:
            print("Top element:",self.stack[-1])

courses= Stack()
courses.push("DLD")
courses.push("OS")
courses.push("CN")

courses.peek()
courses.pop()
courses.peek()