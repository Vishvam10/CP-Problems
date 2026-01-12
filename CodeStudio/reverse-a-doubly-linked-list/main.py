"""
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""


def reverseDLL(head):
    cur = head
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev
        cur.prev = nxt

        prev = cur
        cur = nxt

    return prev
