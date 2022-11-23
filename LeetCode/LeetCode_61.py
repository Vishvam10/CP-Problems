"""
DIFFICULTY : medium
TAGS : linked list, two pointers
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # IDEA : Create a circular linked list and 
    #        cut it at (n-k+1) position where n 
    #        is the length of the linked list
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        n = 1
        while(temp.next):
            temp = temp.next
            n += 1
        k = k % n
        temp.next = head
        temp1 = head
        for i in range(n-k-1):
            temp1 = temp1.next
        
        new_head = temp1.next
        temp1.next = None
        
        return new_head