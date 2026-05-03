class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if data<self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        elif data>self.data:
            self.right.insert(data)

def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
    
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
        