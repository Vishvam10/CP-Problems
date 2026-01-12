class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    if head == None or head.next == None:
        return head
    temp = head
    while temp:
        if (temp.next) and (temp.data == temp.next.data):
            temp1 = temp.next
            temp.next = temp.next.next
            if temp.next and temp.next.next:
                temp.next.next.prev = temp
            del temp1
        else:
            temp = temp.next

    return head
