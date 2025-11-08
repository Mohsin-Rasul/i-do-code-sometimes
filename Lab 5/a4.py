class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        temp = self.head
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def printList(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        print("NULL <-> ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    def getFromEnd(self, n):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        count = 1
        while temp and count < n:
            temp = temp.prev
            count += 1
        
        if temp is None:
            print(f"Error: {n} is out of bounds.")
        else:
            print(f"The {n}-th node from the end is: {temp.data}")

if __name__ == "__main__":
    print("--- Activity 4 ---")
    
    myList = LinkedList()
    myList.add(5)
    myList.add(10)
    myList.add(15)
    myList.add(20)
    myList.add(25)
    
    print("List for A4:")
    myList.printList()
    
    print("\nGetting 3rd node from the end:")
    myList.getFromEnd(3)
    
    print("\nGetting 1st node from the end:")
    myList.getFromEnd(1)
    
    print("\nGetting 5th node from the end:")
    myList.getFromEnd(5)

    print("\nGetting 10th node from the end:")
    myList.getFromEnd(10)