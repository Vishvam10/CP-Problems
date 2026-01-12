class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def rev(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def addOne(head: Node) -> Node:
    rev1 = rev(head)
    temp = rev1

    while temp:
        carry = 0
        if (temp.data) < 9:
            temp.data += 1
            carry = 0
            break
        else:
            temp.data = 0
            carry = 1
        temp = temp.next

    head = rev(rev1)
    if carry == 1:
        nn = Node(1)
        nn.next = head
        head = nn

    return head
