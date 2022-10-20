"""
DIFFICULTY : easy
TAGS : linked list, two pointers, stack, recursion
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head) :
            if not head or not head.next:
                return head

            cur, prev = head, None
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev if prev else head

        slow = fast = head
        
        # Finding the middle node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        ll1, ll2 = head, slow.next
        
        # Reversing the second half
        ll2 = reverse(ll2)
                
        while ll2:
            if not ll1.val == ll2.val:
                return False
            ll2 = ll2.next
            ll1 = ll1.next
        
        return True