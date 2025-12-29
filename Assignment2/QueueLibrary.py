#Implementation of Queue using Library(List)
queue = []

queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

frontElement = queue[0]
print("Peek: ", frontElement)

poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

print("Size: ", len(queue))



'''
Output:
Queue:  ['A', 'B', 'C']
Peek:  A
Dequeue:  A
Queue after Dequeue:  ['B', 'C']
isEmpty:  False
Size:  2
'''