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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        count = 0
        temp1 = temp2 = head

        while temp1:
            count += 1
            temp1 = temp1.next
        
        mid_index = count // 2
        
        for _ in range(mid_index - 1):
            temp2 = temp2.next
        
        temp2.next = temp2.next.next
        return head