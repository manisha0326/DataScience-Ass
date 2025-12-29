#Implementation of Heap using Library(heapq)
import heapq

heap = []
print("Initial Heap:", heap)

heapq.heappush(heap, 30)
print("Push 30:", heap)

heapq.heappush(heap, 10)
print("Push 10:", heap)

heapq.heappush(heap, 20)
print("Push 20:", heap)

smallest = heapq.heappop(heap)
print("Pop Smallest:", smallest)
print("Heap After Pop:", heap)



'''output:
Initial Heap: []
Push 30: [30]
Push 10: [10, 30]
Push 20: [10, 30, 20]
Pop Smallest: 10
Heap After Pop: [20, 30]
'''