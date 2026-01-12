# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        slow = fast = temp = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = reverse(slow)

        while slow:
            if temp.val != slow.val:
                return False
            else:
                temp = temp.next
                slow = slow.next

        return True
