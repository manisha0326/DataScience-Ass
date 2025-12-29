# Implementation of stack using scratch
class Fruits:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

myStack = Fruits()
myStack.push('Mango')
myStack.push('Apple')
myStack.push('Banana')
myStack.push('Orange')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())



'''
Output:
Stack:  ['Mango', 'Apple', 'Banana', 'Orange']
Pop:  Orange
Stack after Pop:  ['Mango', 'Apple', 'Banana']
Peek:  Banana
isEmpty:  False
Size:  3
'''