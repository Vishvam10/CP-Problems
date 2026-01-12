"""
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""


def reverseLinkedList(head):
    # write your code here
    cur = head
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt
    return prev
