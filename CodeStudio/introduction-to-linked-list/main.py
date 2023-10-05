class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    # Write your code here
    head = Node(-1)
    temp = head
    n = len(arr)
    for i in range(len(arr)) :
        temp.next = Node(arr[i])
        temp = temp.next
    return head.next