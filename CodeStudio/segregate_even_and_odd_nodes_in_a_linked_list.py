'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def segregateEvenOdd(head):
    odd, even, odd_st = head, head.next, head
    while(even and even.next) :
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    even.next = odd_st
    return head
    