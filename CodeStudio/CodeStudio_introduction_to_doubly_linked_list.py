class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def constructDLL(arr: [int]) -> Node:
    # Write your code here
    head = Node(-1)
    temp = head
    for x in arr :
        nn = Node(val=x)
        temp.next = nn
        nn.prev = temp
        temp = nn
    return head.next

