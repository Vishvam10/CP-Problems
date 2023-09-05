class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(head: Node) -> Node:
    temp = head
    while(temp.next.next) :
        temp = temp.next
    temp.next = None
    return head