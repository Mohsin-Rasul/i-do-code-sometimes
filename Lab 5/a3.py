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

    def printAddresses(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        print(f"\n{'Node Data':<15} | {'Current Address':<16} | {'Prev Address':<16} | {'Next Address':<16}")
        print("-" * 67)
        
        while temp:
            data = temp.data
            currAddr = id(temp)
            prevAddr = id(temp.prev) if temp.prev else 'NULL'
            nextAddr = id(temp.next) if temp.next else 'NULL'
            
            print(f"{str(data):<15} | {currAddr:<16} | {prevAddr:<16} | {nextAddr:<16}")
            temp = temp.next

if __name__ == "__main__":
    print("--- Activity 3 ---")
    
    studentList = LinkedList()
    
    for i in range(1, 8):
        studentList.add(f"Student_ID_{i}")
    
    print(f"Student list with 7 nodes created.")
    
    studentList.printAddresses()