# Implementation of stack using Library(list)

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after push operation: ", stack)
print("Length after push:", len(stack))

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)
print("Length:", len(stack))

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

print("Size: ",len(stack))


'''
Output:
Stack after push operation:  [10, 20, 30]
Length after push: 3
Peek:  30
Pop:  30
Stack after Pop:  [10, 20]
Length: 2
isEmpty:  False
Size:  2
'''