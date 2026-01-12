"""
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
"""


def detectCycle(head):
    # Write your code here.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # Compares the memory address
        if slow == fast:
            # print('\nslow == fast : ', slow, fast)
            return True
    return False
