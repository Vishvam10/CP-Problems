# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # The loop condition ensures that temp.next.next 
    # always exists
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        while(temp.next) :
            if(temp.next.val == val) :
                temp.next = temp.next.next
            else :
                temp = temp.next
        return dummy.next
                