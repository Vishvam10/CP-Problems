# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while(head) :
            if(head.next and head.val == head.next.val) :
                while(head.next and head.val == head.next.val) :
                    head = head.next
                temp.next = head.next
            else :
                temp = temp.next
            head = head.next
        return dummy.next