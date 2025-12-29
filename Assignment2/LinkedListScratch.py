#Implementation of Linked list using Scratch

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    print("Linked List:", end=" ")
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def insertNodeAtPosition(head, newNode, position):
    print(f"\nInserting {newNode.data} at position {position}...")

    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

def deleteSpecificNode(head, nodeToDelete):
    print(f"\nDeleting node with value {nodeToDelete.data}...")

    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        print("Node not found!")
        return head

    currentNode.next = currentNode.next.next
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List:")
traverseAndPrint(node1)

newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter Insertion:")
traverseAndPrint(node1)

node1 = deleteSpecificNode(node1, node4)

print("\nAfter Deletion:")
traverseAndPrint(node1)