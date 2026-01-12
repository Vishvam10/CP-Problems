class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.


def flattenLinkedList(head: Node) -> Node:
    arr = []
    temp = head
    while temp:
        temp2 = temp
        while temp2:
            arr.append(temp2.data)
            temp2 = temp2.child
        temp = temp.next

    arr = list(sorted(arr))
    if not arr:
        return None

    nh = Node(arr[0])
    temp = nh
    for x in arr[1:]:
        nn = Node(x)
        temp.child = nn
        temp = nn
    return nh
