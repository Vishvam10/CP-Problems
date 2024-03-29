class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.


def insertAtTail(head: Node, k: int) -> Node:
    temp = head
    if (temp == None):
        return Node(val=k)

    while (temp.next):
        temp = temp.next
    nn = Node(val=k)
    temp.next = nn
    nn.prev = temp
    nn.next = None
    return head
