#Implementation of Queue using Scratch
class Animal:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Create a queue
animal = Animal()

animal.enqueue('Cat')
animal.enqueue('Dog')
animal.enqueue('Monkey')

print("Queue: ", animal.queue)
print("Peek: ", animal.peek())
print("Dequeue: ", animal.dequeue())
print("Queue after Dequeue: ", animal.queue)
print("isEmpty: ", animal.isEmpty())
print("Size: ", animal.size())


'''
Output:
Queue:  ['Cat', 'Dog', 'Monkey']
Peek:  Cat
Dequeue:  Cat
Queue after Dequeue:  ['Dog', 'Monkey']
isEmpty:  False
Size:  2
'''