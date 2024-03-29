'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''


def removeKthNode(head, k):
    start = Node(-1)
    start.next = head
    slow, fast = start, start

    for _ in range(k):
        fast = fast.next

    while (fast.next):
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return start.next
