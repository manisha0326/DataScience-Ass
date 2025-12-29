#Implementation of Tree using Scratch
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(50)
root.left = TreeNode(25)
root.right = TreeNode(75)

print("Root:", root.value)
print("Left Child:", root.left.value)
print("Right Child:", root.right.value)


'''Output:
Root: 50
Left Child: 25
Right Child: 75
'''