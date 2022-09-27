# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Store head as temp, move head, update temp.next 
    # to prev ann finally update prev to temp
    
    # RETURN prev NOT head as the nodes are reversed
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while(head) :
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev