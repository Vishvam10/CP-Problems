class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    slow = fast = entry = head
    if (head == None):
        return 0
    if (head.next == head):
        return 1

    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            ans = 0
            slow = slow.next
            while (slow != fast):
                slow = slow.next
                ans += 1
            return ans + 1

    return 0
