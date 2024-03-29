'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''


def length(head):
    n = 0
    while (head):
        n += 1
        head = head.next
    return n
