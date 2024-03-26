inputs = [5, 10, 12, 2, 9, 1]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.head = None
        self.output = [[] for i in range(len(inputs))]
    def insert(self, value, parent=None):
        if self.head == None:
            self.head = Node(value)
        elif parent == None:
            self.insert(value, self.head)
        else:
            if value <= parent.value:
                if parent.left is None:
                    parent.left = Node(value)
                else:
                    self.insert(value, parent.left)
            else:
                if parent.right is None:
                    parent.right = Node(value)
                else:
                    self.insert(value, parent.right)
    def printValues(self, current, count=0):
        if current.left:
            self.printValues(current.left, count+1)
        if current.right:
            self.printValues(current.right, count+1)
        self.output[count].append(current.value)
            
BST = Tree()
for i in inputs:
    BST.insert(i)
BST.printValues(BST.head)
print(BST.output)