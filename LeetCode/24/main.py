"""
DIFFICULTY : medium
TAGS : linked list, recursion
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        prev = dummy
        cur = head
        while cur and cur.next:
            prev.next = cur.next
            # Here, we assign cur.next using prev's pointers because
            # if we used cur's next pointers, then we would need to
            # check if cur.next.next exists.
            cur.next = prev.next.next
            prev.next.next = cur

            prev = cur
            cur = cur.next
        return dummy.next
