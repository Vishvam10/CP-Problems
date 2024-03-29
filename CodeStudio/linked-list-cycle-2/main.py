'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''


def firstNode(head):
    slow = fast = temp = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            while (slow != temp):
                temp = temp.next
                slow = slow.next
            return slow
    return None
