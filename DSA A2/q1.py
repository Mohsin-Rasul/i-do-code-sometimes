class Node:
    def __init__(self, data):
        self.data = data  # The data 
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The list is empty at the start

    def addNode(self, data):
        #This function adds a new node to the end of the list.
        newnode = Node(data)
        if self.head is None:
            # If the list is empty, make the new node the head
            self.head = newnode
            return
        
        # If list is not empty, go to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
        
        # Link the last node to the new node
        temp.next = newnode

    def insertAfter(self, findData, newData):
        
        #This function finds a node with 'findData' and inserts 'newData'
        temp = self.head
        while temp:
            if temp.data == findData:
                # Found the node
                newnode = Node(newData)
                newnode.next = temp.next  # New node points to what temp was pointing to
                temp.next = newnode       # Temp points to the new node
                return
            temp = temp.next
        print(f"Data '{findData}' not found in list.")

    def updateNode(self, findData, appendData):

        #This function finds a node with 'findData' and appends data!
        temp = self.head
        while temp:
            if temp.data == findData:
                # Found the node, update its data
                temp.data = temp.data + appendData
                return
            temp = temp.next
        print(f"Data '{findData}' not found in list.")

    def display(self):
        #This function prints all the data in the list!
        if self.head is None:
            print("List is empty")
            return
            
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# 1. Create the list and add initial data
myList = SinglyLinkedList()
myList.addNode("Name: Mohsin Rasul")
myList.addNode("Registration Number (Reg#): BCY243024")
myList.addNode("Contact Number: 0300-1234567")
myList.addNode("Address: House 1, Street 1, Islamabad")
myList.addNode("Email Address: mohsin@cust.pk")

print("--- Initial List ---")
myList.display()

# 2. Insert Father's Name after Name
myList.insertAfter("Name: Mohsin Rasul", "Father's Name: Faisal Rasul")

# 3. Update Address with postal code
myList.updateNode("Address: House 1, Street 1, Islamabad", ", 44000")

# 4. Display the final list
print("\n--- Final List After Operations ---")
myList.display()
