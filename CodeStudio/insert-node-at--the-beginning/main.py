class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Do not change code above.


def insertAtFirst(head: Node, val: int) -> Node:
    cur = Node(val)
    cur.next = head
    return cur
