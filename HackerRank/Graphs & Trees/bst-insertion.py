class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        if self.root == None:
            self.root = Node(val)
            return self.root
        node = self.root
        next_node = node.left if node.info > val else node.right
        while next_node:
            node = next_node
            next_node = node.left if node.info > val else node.right
        if node.info > val:
            node.left = Node(val)
        else:
            node.right = Node(val)
        return self.root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
