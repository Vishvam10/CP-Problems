# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Total length is now n+1
        # To handle (k == n) case
        
        start = ListNode(-1)
        start.next = head
        slow, fast = start, start

        for _ in range(1, k+1) :
            fast = fast.next
        # Now, fast is at ()k-1)th position from the beginning

        # We go from (k-1) to n => Total traversed : (n-k+1)
        while(fast.next) :
            slow = slow.next
            fast = fast.next
        
        # Now, slow is at (n-k+1)th position from the end
        # So, slow is at (n-(n-k+1)) = (k-1)th position from the beginning

        slow.next = slow.next.next

        return start.next
        
